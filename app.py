from flask import Flask, render_template
# from flask_cors import CORS


app=Flask(__name__)
# CORS(app)

@app.route("/",methods=['GET'])
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

@app.route("/todolist", methods=['POST'])
def todolistF():
    return render_template ('todo_list.html')

if __name__ == '__main__':
    app.run(debug=True)