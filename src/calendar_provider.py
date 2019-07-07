from typing import Any, Dict


class CalendarProvider:
    
    def get_calendar(self, url: str) -> Dict[str, Any]:
        """
        Fetch the content from url
        
        Args:
            url: url of target calendar

        Returns:
            response body in python native form
        """
        return {}
