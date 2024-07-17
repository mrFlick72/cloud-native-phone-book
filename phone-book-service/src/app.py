from flask import Flask

from src.infrastructure.AppConfig import application_init
from src.web.UserNameInjectorFilter import UserNameInjectorFilter
from web.HealthEndPoint import HealthEndPoint

app = Flask(__name__)

user_name_injector_filter = UserNameInjectorFilter()
app.before_request(user_name_injector_filter.filter)
application_init(app)
HealthEndPoint(app)


if __name__ == '__main__':
    app.run(port=5000)




