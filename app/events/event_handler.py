from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event


@local_handler.register(event_name="cat-requested-a-fish")
async def handle_all_cat_events(event: Event):
    """
    this handler will match with an events prefixed with `cat`.
    ex: "cat_eats_a_fish", "cat_is_cute", etc
    """
    event_name, payload = event

    # the `event` argument is nothing more than a tuple of event name and payload
    print("===============================================")
    print(f"Event name: {event_name}")
    print(f"Payload: {payload}")

