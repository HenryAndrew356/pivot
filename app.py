from flask import Flask, render_template

app=Flask(__name__)

person01= [
    {
        'fullname':'',
        'occupation':'',
        'perfil':'',
        'numbertelephone':'',
        'email':''
    }
]

@app.route("/getData")
def getdata():
    name='Andrew Medina Condo'
    return render_template ('index2.html',name=name)

@app.route("/returnCV")
def cv():
    return render_template ('index.html')

@app.route("/workList")
def listado():
    return render_template ('index.html')

if __name__=="__main__":
    app.run(debug=True)

