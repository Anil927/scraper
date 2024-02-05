import logging
import sys

# Create a logger
logger = logging.getLogger('my_logger')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a handler
handler = logging.StreamHandler(sys.stdout)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add the formatter to the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
