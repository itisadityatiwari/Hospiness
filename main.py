from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
    
@app.route("/Adi")
def Adi():
    return "Hello, Aditya"

@app.route("/Poo")
def Poo():
    return "Hello, Pooja"

@app.route("/Home")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)