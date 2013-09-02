from pycclib.cclib import *
from random import randrange
import json


class CData:

    def __init__(self):
        self.api = API()

    def create_token(self, email, password):
        self.api.create_token(email, password)

    def get_apps(self):
        return [i['name'] for i in self.api.read_apps()]

    def _has_default_dep(self, appname):
#        try:
        info = self.api.read_deployment(appname, 'default')
        import pdb; pdb.set_trace()
        print info
        return info
#        except:
#            return False

    def get_info(self, appname):
        state = ['happy', 'sad', 'rainbow', 'ill', 'comatose']
        info = self._has_default_dep(appname)
        print info
        if not info:
            return json.dumps(['comatose'])
        else:
            return json.dumps(state[randrange(len(state)-2)])

    def get_face(self, face):
        return json.dumps([face])

