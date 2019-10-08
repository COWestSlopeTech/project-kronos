#!/usr/bin/env python3
"""
I am the main entry point to this program
"""
from typing import Dict, Any

from src.event_provider import CalendarProvider
from src.event_enricher import EventEnricher
from src.event_parser import EventParser
from src.event_pusher import EventPusher
from src.event_url_provider import EventUrlProvider


def main() -> None:
    """
    I am an orchestrator for all other functionality
    """
    # 1. Gather known event urls
    url_provider = EventUrlProvider()

    # 2. For each url, get contents
    cal_fetcher = CalendarProvider()
    raw_events: Dict[str, Any] = {}
    for name, url in url_provider.get_urls():
        raw_events[name] = cal_fetcher.find_events(url)

    # 3. Parse contents to neutral form
    parser = EventParser()
    parsed_events: Dict[str, Any] = {}
    for name, data in raw_events.items():
        parsed_events[name] = parser.parse(data)

    # 4. Enrich events with additional data
    enricher = EventEnricher()
    for name, data in parsed_events.items():
        enricher.enrich(data)

    # 5. Push events to datastore
    pusher = EventPusher()
    for name, data in parsed_events.items():
        pusher.push(data)

    print(f"Added {len(parsed_events)} events to the datastore")


if __name__ == "__main__":
    # These lines execute only when this file is called from the command line
    main()
