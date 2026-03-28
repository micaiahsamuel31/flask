from flask import Flask, render_template

app = Flask(__name__, template_folder= "templates")

@app.route("/")
def hello_world():
    name = "Samuel"
    return render_template("index.html", a=name)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
