from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

items = []
next_id = 1

@app.route('/')
def home():
    return render_template('index.html', items=items[::-1])

@app.route('/add', methods=['POST'])
def add_item():
    global next_id
    title = request.form.get('title')
    itype = request.form.get('type')
    location = request.form.get('location')
    contact = request.form.get('contact')
    image = request.files.get('image')
    filename = ""
    if image and image.filename!= "":
        filename = f"{next_id}_{secure_filename(image.filename)}"
        image.save(os.path.join(UPLOAD_FOLDER, filename))

    items.append({
        'id': next_id,
        'title': title,
        'type': itype.strip(),
        'location': location,
        'contact': contact,
        'image': filename
    })
    next_id += 1
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    global items
    # delete image file also
    for it in items:
        if it['id'] == item_id and it['image']:
            try:
                os.remove(os.path.join(UPLOAD_FOLDER, it['image']))
            except:
                pass
    items = [i for i in items if i['id']!= item_id]
    return redirect('/')

@app.route('/edit/<int:item_id>', methods=['POST'])
def edit_item(item_id):
    for it in items:
        if it['id'] == item_id:
            it['title'] = request.form.get('title')
            it['type'] = request.form.get('type').strip()
            it['location'] = request.form.get('location')
            it['contact'] = request.form.get('contact')

            image = request.files.get('image')
            if image and image.filename!= "":
                # delete old
                if it['image']:
                    try:
                        os.remove(os.path.join(UPLOAD_FOLDER, it['image']))
                    except:
                        pass
                filename = f"{item_id}_{secure_filename(image.filename)}"
                image.save(os.path.join(UPLOAD_FOLDER, filename))
                it['image'] = filename
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
