from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('../visualization/index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['vidFile']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

print(index())