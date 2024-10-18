from flask import Flask

from infrastructure.AppConfig import application_init
from web.UserNameInjectorFilter import UserNameInjectorFilter
from web.HealthEndPoint import HealthEndPoint

app = Flask(__name__)

user_name_injector_filter = UserNameInjectorFilter()
app.before_request(user_name_injector_filter.filter)
application_init(app)
HealthEndPoint(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




