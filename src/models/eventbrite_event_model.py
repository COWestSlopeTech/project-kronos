import json
from dataclasses import dataclass, asdict
from typing import Optional

from src.models.event_model import Event

@dataclass()
class Eventbrite_Event(Event):

    _status = None
    _capacity = None
    _source_url = None
    _venue_id = None
    _cost = None
    _organization_id = None
    _invite_only = None
    _online_event = None
    _organizer_id = None

    @property
    def status(self) -> Optional[str]:
        return self._status

    @status.setter
    def status(self, value):
        if value is not None:
            assert isinstance(value, str), "Event.status must be an str!"
        self._status = value

    @property
    def capacity(self) -> Optional[int]:
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value is not None:
            assert isinstance(value, int), "Event.capacity must be an int!"
        self._capacity = value

    @property
    def source_url(self) -> Optional[str]:
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        if value is not None:
            assert isinstance(value, str), "Event.source_url must be an str!"
        self._source_url = value

    @property
    def venue_id(self) -> Optional[str]:
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        if value is not None:
            assert isinstance(value, str), "Event.venue_id must be an str!"
        self._venue_id = value

    @property
    def cost(self) -> Optional[int]:
        return self._cost

    @cost.setter
    def cost(self, value):
        if value is not None:
            assert isinstance(value, int), "Event.cost must be an int!"
        self._cost = value

    @property
    def organization_id(self) -> Optional[str]:
        return self._organization_id

    @organization_id.setter
    def organization_id(self, value):
        if value is not None:
            assert isinstance(value, str), "Event.organization_id must be an str!"
        self._organization_id = value

    @property
    def invite_only(self) -> Optional[bool]:
        return self._invite_only

    @invite_only.setter
    def invite_only(self, value):
        if value is not None:
            assert isinstance(value, bool), "Event.invite_only must be an bool!"
        self._invite_only = value

    @property
    def online_event(self) -> Optional[bool]:
        return self._online_event

    @online_event.setter
    def online_event(self, value):
        if value is not None:
            assert isinstance(value, bool), "Event.online_event must be an bool!"
        self._online_event = value

    @property
    def organizer_id(self) -> Optional[str]:
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        if value is not None:
            assert isinstance(value, str), "Event.organizer_id must be an str!"
        self._organizer_id = value

    # @property
    # def img_url(self) -> Optional[str]:
    #     # assert isinstance(self._img_url, str), "Event.img_url must be an str!"
    #     return self._img_url
    #
    # @img_url.setter
    # def img_url(self, value):
    #     # assert isinstance(value, str), "Event.img_url must be an str!"
    #     self._img_url = value
    #
    # @property
    # def logo_url(self) -> Optional[str]:
    #     assert isinstance(self._logo_url, str), "Event.logo_url must be an str!"
    #     return self._logo_url
    #
    # @logo_url.setter
    # def logo_url(self, value):
    #     assert isinstance(value, str), "Event.logo_url must be an str!"
    #     self._logo_url = value


    def to_json(self) -> object:

        obj = json.loads( super().to_json() )

        obj["status"] = self.status
        obj["capacity"] = self.capacity
        obj["source_url"] = self.source_url
        obj["venue_id"] = self.venue_id
        obj["cost"] = self.cost
        obj["organization_id"] = self.organization_id
        obj["invite_only"] = self.invite_only
        obj["status"] = self.status
        obj["online_event"] = self.online_event
        obj["organizer_id"] = self.organizer_id
        # obj["img_url"] = self.img_url
        # obj["logo_url"] = self.logo_url
        # TODO: Determine what options we have for getting image and logo urls

        return json.dumps(obj)