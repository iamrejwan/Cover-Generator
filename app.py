from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = "secret_key"  # For storing session data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    session["data"] = request.form.to_dict()  # Store form data in session
    return {"message": "Preview ready"}

@app.route("/preview")
def preview():
    data = session.get("data", {})
    return render_template("template.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
