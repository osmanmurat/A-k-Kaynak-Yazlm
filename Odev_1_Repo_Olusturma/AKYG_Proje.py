from flask import Flask, jsonify, request

app = Flask(__name__)

# Örnek veri
tasks = [
    {
        'id': 1,
        'title': 'Görev 1',
        'description': 'Bu bir örnek görev',
        'done': False
    },
    {
        'id': 2,
        'title': 'Görev 2',
        'description': 'Bu da başka bir örnek görev',
        'done': False
    }
]

# Tüm görevleri getiren endpoint
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Belirli bir görevi getiren endpoint
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Görev bulunamadı!'}), 404
    return jsonify({'task': task[0]})

# Yeni görev ekleyen endpoint
@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'Eksik veri!'}), 400
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
