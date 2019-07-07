from typing import Any, Dict


class EventPusher:
    
    def push(self, data: Dict[str, Any]) -> None:
        """
        I push well-formed events to our data store
        
        Args:
            data: a well-formed calendar event (in datastore format)
        """
        pass
