from typing import Tuple, Union

from classic.http_api import App
from classic.http_auth import Authenticator

from application import services
from . import auth, controllers


def create_app(is_dev_mode: bool,
               allow_origins: Union[str, Tuple[str, ...]],
               books_manager: services.BooksManager, ) -> App:

    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)
    authenticator.set_strategies(auth.jwt_strategy)
    app = App(prefix='/api')
    app.register(controllers.Books(authenticator=authenticator, books_manager=books_manager))
    return app
