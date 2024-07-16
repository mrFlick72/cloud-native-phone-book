from flask import Flask

from infrastructure.AppConfig import application_init
from web.HealthEndPoint import HealthEndPoint
from web.UserNameInjectorFilter import UserNameInjectorFilter

app = Flask(__name__)

HealthEndPoint(app)
user_nameInjector_filter = UserNameInjectorFilter()
app.before_request(user_nameInjector_filter.filter)
application_init(app)

if __name__ == '__main__':
    app.run()
