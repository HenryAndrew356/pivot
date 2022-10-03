from flask import Flask, render_template

app=Flask(__name__)


@app.route("/formcv")
def form():
    return render_template ('formCV.html')

@app.route("/cvexample")
def examplecv():
    return render_template ('cvexample.html')

@app.route("/returnCV")
def cv():
    return render_template ('cv.html')

if __name__=="__main__":
    app.run(debug=True)

