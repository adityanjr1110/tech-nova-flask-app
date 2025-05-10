from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <head>
                <title>TechNova App</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        text-align: center;
                        padding-top: 50px;
                    }
                    h1 {
                        color: #2c3e50;
                    }
                    p {
                        color: #555;
                        font-size: 20px;
                    }
                </style>
            </head>
            <body>
                <h1>🚀 Hello, TechNova!</h1>
                <p>Welcome to our Flask-powered web app.</p>
                <p>Focused on providing more reliable solutions.</p>
                <p><a href="/about">Learn more</a></p>
            </body>
        </html>
    '''

@app.route('/about')
def about():
    return '''
        <html>
            <head>
                <title>About TechNova</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #e6f7ff;
                        text-align: center;
                        padding-top: 50px;
                    }
                    h1 {
                        color: #0077b6;
                    }
                    p {
                        color: #333;
                        font-size: 16px;
                        width: 60%;
                        margin: auto;
                    }
                </style>
            </head>
            <body>
                <h1>About TechNova</h1>
                <p>TechNova is a software development company focused on building smart inventory management solutions using modern DevOps workflows.</p>
                <p><a href="/">Back to Home</a></p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

