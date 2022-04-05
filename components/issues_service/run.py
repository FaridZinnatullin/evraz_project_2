from wsgiref import simple_server
from composites.api import app

httpd = simple_server.make_server('0.0.0.0', 8002, app)
httpd.serve_forever()
