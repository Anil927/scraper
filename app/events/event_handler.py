"""
This file is an example of how to create a local event handler.

The `local_handler` is a global instance of `EventHandler` that is used to register event handlers.
It can be accessed from anywhere in the application.

"""
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event


@local_handler.register(event_name="cat-requested-a-fish")
async def handle_all_cat_events(event: Event):
    """
    This function is an example of how to handle events.
    This handler will be called whenever an event with the name "cat-requested-a-fish" is dispatched.
    We can then do whatever we want with the event payload. In this case, it's just printed out.

    Args:
        event: The event to be handled.It contains the event name and the payload.
    """
    event_name, payload = event

    # the `event` argument is nothing more than a tuple of event name and payload
    print("===============================================")
    print(f"Event name: {event_name}")
    print(f"Payload: {payload}")

