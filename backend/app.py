from flask import Flask, request, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/merged_files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "Backend for txt merger"

@app.route('/merge', methods=['POST'])
def merge_files():
    uploaded_files = request.files.getlist('files')
    if not uploaded_files:
        return "No files uploaded", 400

    merged_content = ""
    for file in uploaded_files:
        merged_content += file.read().decode('utf-8') + "\n"

    merged_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.txt')
    with open(merged_file_path, 'w') as merged_file:
        merged_file.write(merged_content)

    return send_file(merged_file_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
