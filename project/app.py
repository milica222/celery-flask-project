from flask import Flask, jsonify, request
from celery import Celery
import time
import random

# Flask aplikacija
app = Flask(__name__)

# Konfiguracija Celery-a sa Redisom
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

# Inicijalizacija Celery-a
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Asinhroni zadatak za Monte Carlo metodu
@celery.task
def calculate_pi(num_samples):
    """Asinhroni zadatak koji koristi Monte Carlo metodu za aproksimaciju PI."""
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / num_samples) * 4
    time.sleep(20)
    return f"Aproksimacija PI je {pi_estimate} sa {num_samples} uzoraka."

# API endpoint za pokretanje zadatka
@app.route('/run-task', methods=['POST'])
def run_task():
    data = request.get_json()
    num_samples = data.get('num_samples', 10000)  # Preuzimamo broj uzoraka iz zahteva
    task = calculate_pi.apply_async(args=[num_samples])  # Pokrećemo zadatak asinhrono
    return jsonify({'task_id': task.id}), 202

# API endpoint za proveru rezultata zadatka
@app.route('/task-status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = calculate_pi.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': task.state, 'status': 'Jos uvek nije zapocet...'}
    elif task.state != 'FAILURE':
        response = {'state': task.state, 'result': task.result}
    else:
        response = {'state': task.state, 'status': str(task.info)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
