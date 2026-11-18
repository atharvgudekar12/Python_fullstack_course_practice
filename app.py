from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    project=""
    cgpa=""
    role=""

    if request.method == "POST":
        name = request.form["username"]
        project = request.form["project"]
        cgpa = request.form["cgpa"]
        role = request.form["role"]

    return render_template("index.html", name=name, project=project, cgpa=cgpa, role=role)
    # return render_template("index.html", project=project)
    # return render_template("index.html", cgpa=cgpa)
    # return render_template("index.html", destination=role)

if __name__ == "__main__":
    app.run(debug=True)
