from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Cloud App</title>

        <style>
            body{
                background:#0f172a;
                color:white;
                text-align:center;
                font-family:Arial;
                padding-top:120px;
            }

            .box{
                background:#1e293b;
                width:400px;
                margin:auto;
                padding:30px;
                border-radius:15px;
                box-shadow:0px 0px 15px cyan;
            }

            h1{
                color:cyan;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>Hello Cloud ☁️</h1>
            <p>Flask App Successfully Deployed on Render</p>
        </div>

    </body>
    </html>
    """

@app.route("/about")
def about():
    return "Cloud Computing Practical using Flask + Render"

if __name__ == "__main__":
    app.run(debug=True)
