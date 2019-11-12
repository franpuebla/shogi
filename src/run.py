#!/usr/bin/env python

from api import app


if __name__ == '__main__':
    app.run(
        host=       app.config['GENERAL']['host'],
        port=       int(app.config['GENERAL']['port']),
        threaded =  int(app.config['GENERAL']['threaded'])
    )
