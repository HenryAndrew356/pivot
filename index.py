from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def front():
    return render_template ('frontPage.html')

@app.route("/formOFcv", methods=['POST'])
def formcvPage():
    return render_template ('formCV.html')

@app.route("/cvexample", methods=['POST'])
def cvclone():
    return render_template ('cvClone.html')

@app.route("/returncv", methods=['POST'])
def formofcv():
    return render_template ('cvOfForm.html')

@app.route("/todolist", methods=['POST'])
def todolistF():
    return render_template ('todo_list.html')

if __name__=="__main__":
    app.run(debug=True)



