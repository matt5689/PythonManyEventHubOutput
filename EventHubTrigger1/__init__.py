from typing import List
import logging

import azure.functions as func


def main(events: List[func.EventHubEvent]):
    eventsList= []
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
        eventsList.append(event.get_body().decode('utf-8'))
    
    return eventsList

# def main(events: List[func.EventHubEvent]) -> str:
#     return [events[0].get_body().decode('utf-8'), events[1].get_body().decode('utf-8')]
