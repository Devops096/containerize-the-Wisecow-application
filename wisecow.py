from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body>
        <h1>Welcome to Wisecow</h1>
        <img src="/static/images/wisecow.png" alt="Wisecow">
    </body>
    </html>
    '''

@app.route('/static/images/<path:filename>')
def static_files(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
