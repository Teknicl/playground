from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html",num=3,color="#9FC5F8")

@app.route('/play/<int:x>')
def value(x):
    return render_template("index.html",num=x)

@app.route('/play/<int:x>/<string:cor>')
def color(x,cor):
    return render_template("index.html",num=x,color=cor)

@app.route('/<path:path>')
def catchall(path):
    return "Invalid URL."

if __name__=="__main__":
    app.run(debug=True)