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
            return "This menu does not exists"

    index.exposed = True

cherrypy.quickstart(HungryBot())

