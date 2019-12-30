from src.models.event-model import 

class Eventbrite_Event:

    def __init__(self,
                 Event
                 ):

        self.source = source
        self.source_id = source_id
        self.name = name
        self.description = description
        self.source_url = source_url
        self.start_time = start_time # {'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}
        self.end_time = end_time # {'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}
        self.organization_id = organization_id
        self.capacity = capacity
        self.status = status
        self.invite_only = invite_only
        self.online_event = online_event
        self.cost = cost
        self.organizer_id = organizer_id
        self.venue_id = venue_id
        self.img_url = img_url
        self.logo_url = logo_url