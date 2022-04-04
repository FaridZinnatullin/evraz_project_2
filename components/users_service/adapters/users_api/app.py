from typing import Tuple, Union

from classic.http_api import App
from classic.http_auth import Authenticator

from application import services
from . import auth, controllers


def create_app(is_dev_mode: bool,
               allow_origins: Union[str, Tuple[str, ...]],
               users_manager: services.UsersManager, ) -> App:

    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    authenticator.set_strategies(auth.jwt_strategy)
    app = App(prefix='/api')
    app.register(controllers.Users(authenticator=authenticator, users_manager=users_manager))
    return app
