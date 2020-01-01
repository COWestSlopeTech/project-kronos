import json
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=False)
class Event:
    source: str  # One of constants.EVENT_SOURCE
    source_id: str  # Unique ID from the source
    name: str



    # {'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}
    @property
    def start_time(self) -> Optional[str]:
        assert isinstance(self._start_time, str), 'Event.start_time must be an str!'
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        assert isinstance(value, str), 'Event.start_time must be an str!'
        self._start_time = value


    # {'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}
    @property
    def end_time(self) -> Optional[str]:
        assert isinstance(self._end_time, str), 'Event.end_time must be an str!'
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        assert isinstance(value, str), 'Event.end_time must be an str!'
        self._end_time = value


    @property
    def description(self) -> Optional[str]:
        assert isinstance(self._description, str), 'Event.description must be an str!'
        return self._description

    @description.setter
    def description(self, value):
        assert isinstance(value, str), 'Event.description must be an str!'
        self._description = value


    # @classmethod
    # def new(cls, arg: str) -> "Event":
    #     """
    #
    #     :param arg:
    #     :return:
    #     """
    #
    #     pass

    def to_json(self):
        obj = {
            "source_id": self.source_id,
            "source": self.source,
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "description": self.description
        }
        return json.dumps(obj)


#TODO: Steeve's telling me to write a test for this