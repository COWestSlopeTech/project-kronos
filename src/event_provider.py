from abc import ABC, abstractmethod
from typing import Any, Dict


class EventProviderABC(ABC):
    """
    I define the contract that all providers must implement
    """

    @abstractmethod
    def find_events(self, query_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetch the content from url
        
        Args:
            query_params: describe type of search

        Returns:
            response body in python native form
        """
        raise NotImplementedError
