from flask import Flask

from infrastructure.AppConfig import application_init
from web.HealthEndPoint import HealthEndPoint
from web.UserNameInjectorFilter import UserNameInjectorFilter

app = Flask(__name__)
actuatorApp = Flask(__name__)

HealthEndPoint(actuatorApp)
user_nameInjector_filter = UserNameInjectorFilter()
app.before_request(user_nameInjector_filter.filter)
application_init(app)

if __name__ == '__main__':
    port = 5000
    app.run(port=5000)
    actuatorApp.run(port=port + 1)
