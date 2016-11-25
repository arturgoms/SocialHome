from app import app
from app import INI
from app import BASE_DIR
from gevent.wsgi import WSGIServer

if __name__ == '__main__':
    #app.run(debug=INI[0], host=INI[1], port=INI[2])
    http_server = WSGIServer(('', port=INI[2]), app)
    http_server.serve_forever()
