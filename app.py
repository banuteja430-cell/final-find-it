@app.route('/add', methods=['POST'])
def add_item():
    global next_id
    # CAPTCHA CHECK - IDI FUNCTION LOPALA UNDALI
    if request.form.get('captcha') != '8':
        return "<h3>Wrong Captcha! Type 8</h3><a href='/'>Back</a>"
    
    title = request.form.get('title')
    itype = request.form.get('type')
    location = request.form.get('location')
    contact = request.form.get('contact')
    image = request.files.get('image')
    filename = ""
    if image and image.filename != "":
        filename = f"{next_id}_{secure_filename(image.filename)}"
        image.save(os.path.join(UPLOAD_FOLDER, filename))
    items.append({'id': next_id, 'title': title, 'type': itype.strip(), 'location': location, 'contact': contact, 'image': filename})
    next_id += 1
    return redirect('/')
