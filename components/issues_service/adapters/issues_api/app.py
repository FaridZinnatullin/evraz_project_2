from typing import Tuple, Union

from classic.http_api import App
from classic.http_auth import Authenticator

from application import services
from . import auth, controllers


def create_app(issues_manager: services.IssuesManager, ) -> App:

    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    authenticator.set_strategies(auth.jwt_strategy)
    app = App(prefix='/api')
    app.register(controllers.Issues(authenticator=authenticator, issues_manager=issues_manager))
    return app
