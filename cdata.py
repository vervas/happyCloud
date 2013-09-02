from pycclib.cclib import *


class CData:

    def __init__(self):
        self.api = API()

    def create_token(self, email, password):
        self.api.create_token(email, password)

    def get_apps(self):
        return [i['name'] for i in self.api.read_apps()]

    def has_default_dep(self, appname):
        try:
            return self.api.read_deployment(appname, 'default')
        except:
            return False

