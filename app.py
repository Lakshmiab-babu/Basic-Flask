from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Hello ,This is my custom page</h1>
            <p>This is a Flask web application.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
    
