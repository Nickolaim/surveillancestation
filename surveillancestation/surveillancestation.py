import json
import logging

from .api import Api
from .info import Info
from .camera import Camera
from .action_rule import ActionRule
from .notification import Notification

class Surveillancestation:
    def __init__(self, host, user, passwd):
        self._api = Api(host=host, user=user, passwd=passwd)

        # API list
        self._api_info = Info(self._api)
        self._api_camera = Camera(self._api)
        self._api_action_rule = ActionRule(self._api)
        self._api_notification = Notification(self._api)

    def logout(self):
        self._api.logout()

    @property
    def info(self) -> Info:
        return self._api_info

    @property
    def camera(self) -> Camera:
        return self._api_camera

    @property
    def action_rule(self) -> ActionRule:
        return self._api_action_rule

    @property
    def notification(self) -> Notification:
        return self._api_notification


SurveillanceStation = Surveillancestation
