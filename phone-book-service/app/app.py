from flask import Flask

from infrastructure.AppConfig import application_init

app = Flask(__name__)

application_init(app)

if __name__ == '__main__':
    app.run()
