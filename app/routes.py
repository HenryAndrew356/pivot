from flask import render_template, jsonify, request
from app import app
from app import database as db_helper

@app.route("/", methods=['GET'])
def front():
    return render_template ('frontPage.html')

@app.route("/formOFcv", methods=['GET','POST'])
def formcvPage():
    return render_template ('formCV.html')

@app.route("/cvexample", methods=['POST'])
def cvclone():
    return render_template ('cvClone.html')

@app.route("/returncv", methods=['GET','POST'])
def formofcv():
    return render_template ('cvOfForm.html')

@app.route("/test01", methods=['GET','POST'])
def test():
    return render_template ('testHTML.html')


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/todoList", methods=['POST','GET'])
def pageTodoList():
    items = db_helper.fetch_todo()
    return render_template("todoList.html", items=items)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)