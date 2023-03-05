import datetime
import io
from flask import Flask, request, render_template, redirect, url_for, session
from ocr import *
from flask import jsonify

app = Flask(__name__)

# Secret key for sessions encryption
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
    return render_template("index.html", title="Image Reader")


@app.route('/', methods=['GET', 'POST'])
def scan_file():
    if request.method == 'POST':
        start_time = datetime.datetime.now()
        image_data = request.files['file'].read()
        res = Vision(image_data)
        print(res)
        return jsonify(res)
    # return redirect(url_for('result'))


@app.route('/result')
def result():
    if "data" in session:
        data = session['data']
        return render_template(
            "result.html",
            title="Result",
            time=data["time"],
            text=data["text"],
            words=len(data["text"].split(" "))
        )
    else:
        return "Wrong request method."


if __name__ == '__main__':
    app.run(debug=True)