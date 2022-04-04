from wsgiref import simple_server
from composites.api import app

httpd = simple_server.make_server('0.0.0.0', 5678, app)
httpd.serve_forever()
