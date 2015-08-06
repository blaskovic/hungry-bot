#!/usr/bin/python

import cherrypy
import os
import subprocess

class HungryBot(object):

    def index(self, menu):
        script = '../restaurants/' + str(menu)
        if os.path.isfile(script):
            out = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE).stdout.read()
            return out
        else:
            return "Menu " + str(menu) + " does not exist. Use 'menu list' for the list or submit a patch: https://github.com/blaskovic/hungry-bot"

    index.exposed = True

cherrypy.config.update({'server.socket_port': 8099, 'server.socket_host': '0.0.0.0'})
cherrypy.engine.restart()
cherrypy.quickstart(HungryBot())

