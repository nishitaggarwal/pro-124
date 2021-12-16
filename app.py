from flask import Flask,jsonify,request 

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'Name':'Nishit',
        'Contact': '0123456789',
        'done':False
    },
    {
        'id':2,
        'Name':'Kashvi',
        'Contact': '9876543210',
        'done':False
    },
]

@app.route('/add-contact', methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({'status':"error", 'message':'Please provide the data'},400)
    task = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({'status':'Success', 'message':'Data added successfully'})

@app.route('/get-data')
def get_data():
    return jsonify({
        'data':tasks
    })
    
if __name__ == '__main__':
    app.run()