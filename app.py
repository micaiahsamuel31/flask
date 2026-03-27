from flask import Flask, render_template

app = Flask(__name__, template_folder= "templates")

@app.route("/")
def hello_world():
    name = "Micaiah Samuel"
    roll_no = "25bce7644"
    email = "micaiahsamuel31@gmail.com"
    return render_template("index.html", a=name, b=roll_no, c=email)

'''# Add these lines to print to the terminal and start the server
@app.route("/greet/<name>")
def greet(name):
    return f"HELLO, {name}!'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
