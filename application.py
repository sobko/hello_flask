from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER='/home/ubuntu/workspace/fileupload/files/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        print(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        name = request.form.get("name")
        print(name)
        if request.form.get("quest") == "grail":
            quest = "seek the grail"
        else:
            quest = "join the ratrace"
        color = request.form.get("color")
        if color == "oops":
            return render_template("oops.html", name = name)
        else:
            return render_template("cross.html", name = name, quest = quest)
    else:
        return render_template("index.html")

