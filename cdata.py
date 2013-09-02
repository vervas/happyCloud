from pycclib.cclib import *


class CData:

    def __init__(self):
        self.api = API()

    def create_token(email,password):
        self.api.create_token(email,password)

    def get_apps():
        return api.read_apps()
