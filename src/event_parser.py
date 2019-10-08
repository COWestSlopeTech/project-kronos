from typing import Dict, Any, List


class EventParser:
    def parse(self, calendar: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        I parse raw event data into a neutral form
        
        If given a google calendar, I transform the raw data into our datastore
        format.
        
        Args:
            calendar:

        Returns:
            a list of calendar items in our event datastore format
        """
        return [{}]
