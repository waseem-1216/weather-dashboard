from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is a very simple UI using HTML
    return """
    <h1>My Weather Dashboard ☁️</h1>
    <p>Current Status: <b>Online</b></p>
    <p>DevOps Step: Application Development ✅</p>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')