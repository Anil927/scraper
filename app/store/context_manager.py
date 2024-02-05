from contextlib import contextmanager
from typing import Generator


@contextmanager
def data_store_context_for_every_page() -> Generator[dict ,None, None]:
    yield {}



