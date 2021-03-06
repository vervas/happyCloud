from pycclib.cclib import *
from datetime import datetime, timedelta
import time
import json
from flask import Response


class CData:

    def __init__(self):
        self.api = API()

    def create_token(self, email, password):
        self.api.create_token(email, password)

    def get_apps(self):
        return [i['name'] for i in self.api.read_apps()]

    def _has_default_dep(self, appname):
       try:
            return json.dumps(self.api.read_deployment(appname, 'default'))
       except:
           return False

    def _hours_since_last_deployment(self, appname):
        current_time = time.mktime(time.localtime())
        last_deploy = self.api.read_log(appname, 'default', 'deploy')[-1]['time']
        return int((current_time - last_deploy) / 60 / 60)

    def _request_number(self, appname, hours=24):
        period = datetime.today()-timedelta(hours=hours)
        return len(self.api.read_log(appname, 'default', 'access', last_time=period))

    def _errors_percentage(self, appname):
        request_no = self._request_number(appname)
        bad_request_no = len([i['status'] for i in self.api.read_log(appname,'default','access') if int(i['status'])>399])

        return float(bad_request_no)/request_no

    def _measure_state(self, appname):
        state = 'euphoric'
        if self._hours_since_last_deployment(appname) > 24:
            state = 'happy'
        if self._errors_percentage(appname) > 0.1:
            state = 'buggy'

        return state

    def get_info(self, appname):
        """
            state = ['happy', 'sad', 'rainbow', 'ill', 'comatose']
        """
        info = self._has_default_dep(appname)
        if not info:
            return Response(json.dumps([{'state': 'comatose'}]))
        else:
            return Response(json.dumps(
                [
                    {
                        'state': self._measure_state(appname),
                        'data': {
                            'hours_since_last_dep': self._hours_since_last_deployment(appname),
                            'error_percentage': self._errors_percentage(appname),
                            'requests_last_24': self._request_number(appname),
                            'requests_last_48': self._request_number(appname,48)
                        }
                    }
                ]
            ))
