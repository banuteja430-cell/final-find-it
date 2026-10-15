from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['photo']
    item_type = request.form['type']
    name = request.form['name']
    contact = request.form['contact']
    
    if file.filename == '':
        return "Photo select cheyyi bro!"
    
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    
    return f"""
    <h2 style="font-family:Arial;text-align:center;margin-top:50px;">
    ✅ {item_type} Upload Success!<br><br>
    Name: {name}<br>
    Contact: {contact}<br><br>
    FindIt lo save ayindi. Match dorikithe message vastundi!<br><br>
    <a href='/'>Back to Home</a>
    </h2>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
