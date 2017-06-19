from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Bello World!"

if __name__ == "__main__":
    application.run()
