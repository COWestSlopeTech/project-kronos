from typing import Any, Dict
from src.constants.constants import EVENT_SOURCE, EVENT_STATUS
from src.models.event_model import Event
from src.models.eventbrite_event_model import Eventbrite_Event



class EventEnricher:
    def enrich(self, data: Dict[str, Any], source: str) -> Dict[str, Any]:
        """
        I provide additional data for an event

        The data is enriched in-place, but also returned for convenience

        Args:
            data: calendar data in our datastore format

        Returns:
            enriched data
        """

        encoded_data = []
        for ev in data:

            if(source == EVENT_SOURCE["EVENT_BRITE"]):

                event = Eventbrite_Event( EVENT_SOURCE["EVENT_BRITE"], ev["id"], ev["name"]["text"] )

                # Optionals
                event.__setattr__("start_time", "{'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}" )
                event.__setattr__("end_time", "{'timezone': 'America/Denver', 'local': '2020-02-07T19:00:00', 'utc': '2020-02-08T02:00:00Z'}" )
                event.__setattr__("description", ev["description"]["text"])

                event.__setattr__("capacity", ev["capacity"])
                event.__setattr__("source_url", ev["resource_uri"])
                event.__setattr__("venue_id", ev["venue_id"])
                event.__setattr__("organization_id", ev["organization_id"])
                event.__setattr__("invite_only", ev["invite_only"])
                event.__setattr__("online_event", ev["online_event"])
                event.__setattr__("organizer_id", ev["organizer_id"])
                # event.__setattr__("image_url", ev["image_url"])
                # event.__setattr__("logo_url", ev["logo_id"])

                if( ev["is_free"] ):
                    event.__setattr__("cost", 0)
                else:
                    event.__setattr__("cost", ev["is_free"])


                if( ev["status"] == "live"):
                    event.__setattr__("status", EVENT_STATUS["ACTIVE"])
                else:
                    # TODO: determine all status types from EventBrite to set status more precisely
                    event.__setattr__("status", EVENT_STATUS["INACTIVE"])

                encoded_data.append(event)

                print("--> ", event.to_json())

            elif(EVENT_SOURCE["GOOGLE"]):
                print("TODO: Support Google enriching")
                # ev["source"] = source

        return encoded_data

