from pycclib.cclib import *
import time
import json


class CData:

    def __init__(self):
        self.api = API()

    def create_token(self, email, password):
        self.api.create_token(email, password)

    def get_apps(self):
        return [i['name'] for i in self.api.read_apps()]

    def _has_default_dep(self, appname):
        try:
            return self.api.read_deployment(appname, 'default')
        except:
            return False

    def _hours_since_last_deployment(self, appname):
        current_time = time.mktime(time.localtime())
        last_deploy = self.api.read_log(appname, 'default', 'deploy')[-1]['time']
        return int((current_time - last_deploy) / 60 / 60)

    def _errors_percentage(self, appname, period=None):
        request_no = len(self.api.read_log(appname, 'default', 'access', last_time=period))
        bad_request_no = len([i['status'] for i in self.api.read_log('rainbowapp','default','access') if int(i['status'])>399])

        return float(bad_request_no)/request_no

    def _measure_state(self, appname):
        state = 'rainbow'
        if self._hours_since_last_deployment(appname) > 24:
            state = 'happy'
        if self._errors_percentage(appname) > 0.1:
            state = 'ill'

        return state

    def get_info(self, appname):
        """
            state = ['happy', 'sad', 'rainbow', 'ill', 'comatose']
        """
        info = self._has_default_dep(appname)
        if not info:
            return json.dumps([{'state': 'comatose'}])
        else:
            return json.dumps([{'state': self._measure_state(appname)}])
