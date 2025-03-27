import pickle
from flask import Flask, request,send_file
import io
import random
app = Flask(__name__)

class Cat:
    def __init__(self, name, cuteness):
        self.name = name
        self.cuteness = cuteness
    def __str__(self):
        return f"Cat named {self.name}. Cuteness level: {self.cuteness}"
    def meow(self):
        return random.choice(["Meow", "Purr", "Hiss"])
@app.route('/download', methods=['GET'])
def download():
    cat = Cat("Tsukimi", 100)
    serialized_cat = pickle.dumps(cat)
    return send_file(
        io.BytesIO(serialized_cat),
        as_attachment=True,
        download_name='cat.pickle',
        mimetype='application/octet-stream'
    )
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return '''
        <h1>CAT Scan</h1>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
            <a href="/download">Download sample cat</a>
        '''
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400
    print(file)
    serialized_cat = file.read()
    print(serialized_cat)
    print("----")
    cat = pickle.loads(serialized_cat)

    with open('version.txt', 'r') as f:
        version = f.read()

    return f"Loaded {cat}. Version: {version}"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=7777)