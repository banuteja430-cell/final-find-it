from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
items = []
@app.route('/')
def home():
    return render_template('index.html', items=items[::-1])
@app.route('/add', methods=['POST'])
def add_item():
    title = request.form.get('title')
    itype = request.form.get('type')
    location = request.form.get('location')
    contact = request.form.get('contact')
    image = request.files.get('image')
    filename = ""
    if image and image.filename != "":
        filename = image.filename
        image.save(os.path.join(UPLOAD_FOLDER, filename))
    items.append({'title': title, 'type': itype, 'location': location, 'contact': contact, 'image': filename})
    return redirect('/')
