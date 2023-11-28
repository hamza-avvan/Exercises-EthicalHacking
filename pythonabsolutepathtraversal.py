from flask import abort, Flask, request, send_file 
import os
app = Flask (__name__)

@app.route('/download')
def download():
    file = request.args.get('file', 'default.png')
    
    if '..' in file:
        abort (400, 'Directory Traversal Detected')
    
    absolute_path = os.path.join(app.root_path, 'downloads', file)

    if os.path.isfile(absolute_path):
        return send_file (absolute_path)
    else:
        abort (404, 'Requested File Not Found')
