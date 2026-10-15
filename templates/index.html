from flask import Flask, render_template, request, redirect
import os, sqlite3
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_db():
    conn = sqlite3.connect('findit.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, type TEXT, location TEXT, contact TEXT, image TEXT, email TEXT, instagram TEXT)''')
    # Add new columns if old DB exists
    try: c.execute("ALTER TABLE items ADD COLUMN email TEXT")
    except: pass
    try: c.execute("ALTER TABLE items ADD COLUMN instagram TEXT")
    except: pass
    conn.commit()
    conn.close()
init_db()

def get_items(filter_type='All', search=''):
    conn = sqlite3.connect('findit.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = "SELECT * FROM items"
    params = []
    conds = []
    if filter_type not in ['All','Post']:
        conds.append("type = ?")
        params.append(filter_type)
    if search:
        conds.append("(title LIKE ? OR location LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%"])
    if conds:
        query += " WHERE " + " AND ".join(conds)
    query += " ORDER BY id DESC"
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows

def find_match(title, itype):
    conn = sqlite3.connect('findit.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    opposite = "Found" if itype == "Lost" else "Lost"
    keywords = title.lower().split()
    for kw in keywords:
        if len(kw) < 3: continue
        c.execute("SELECT * FROM items WHERE type=? AND LOWER(title) LIKE ?", (opposite, f"%{kw}%"))
        match = c.fetchone()
        if match:
            conn.close()
            return match
    conn.close()
    return None

@app.route('/')
def home():
    q = request.args.get('q', '')
    f_type = request.args.get('type', 'All')
    matched_title = request.args.get('matched_title', '')
    matched_contact = request.args.get('matched_contact', '')
    matched_location = request.args.get('matched_location', '')
    matched_email = request.args.get('matched_email', '')
    matched_insta = request.args.get('matched_insta', '')
    items = get_items(f_type, q)
    all_items = get_items()
    total = len(all_items)
    lost = len([i for i in all_items if i['type'] == 'Lost'])
    found = len([i for i in all_items if i['type'] == 'Found'])
    rate = int((found/total*100) if total>0 else 78)
    return render_template('index.html', items=items, total=total, lost=lost, found=found, rate=rate, q=q, f_type=f_type,
                           matched_title=matched_title, matched_contact=matched_contact, matched_location=matched_location,
                           matched_email=matched_email, matched_insta=matched_insta)

@app.route('/add', methods=['POST'])
def add_item():
    title = request.form.get('title')
    itype = request.form.get('type')
    location = request.form.get('location')
    contact = request.form.get('contact')
    email = request.form.get('email','')
    instagram = request.form.get('instagram','')
    image = request.files.get('image')
    filename = ""
    if image and image.filename != "":
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))
    
    match = find_match(title, itype)

    conn = sqlite3.connect('findit.db')
    c = conn.cursor()
    c.execute("INSERT INTO items (title,type,location,contact,image,email,instagram) VALUES (?,?,?,?,?,?,?)", 
              (title, itype, location, contact, filename, email, instagram))
    conn.commit()
    conn.close()

    if match:
        return redirect(f"/?matched_title={match['title']}&matched_contact={match['contact']}&matched_location={match['location']}&matched_email={match['email'] or ''}&matched_insta={match['instagram'] or ''}&type=Post")
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = sqlite3.connect('findit.db')
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:item_id>')
def edit_page(item_id):
    conn = sqlite3.connect('findit.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE id=?", (item_id,))
    item = c.fetchone()
    conn.close()
    return render_template('edit.html', item=item)

@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    title = request.form.get('title')
    itype = request.form.get('type')
    location = request.form.get('location')
    contact = request.form.get('contact')
    email = request.form.get('email','')
    instagram = request.form.get('instagram','')
    image = request.files.get('image')
    conn = sqlite3.connect('findit.db')
    c = conn.cursor()
    if image and image.filename != "":
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))
        c.execute("UPDATE items SET title=?, type=?, location=?, contact=?, image=?, email=?, instagram=? WHERE id=?", (title, itype, location, contact, filename, email, instagram, item_id))
    else:
        c.execute("UPDATE items SET title=?, type=?, location=?, contact=?, email=?, instagram=? WHERE id=?", (title, itype, location, contact, email, instagram, item_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
