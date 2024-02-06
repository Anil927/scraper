from enum import Enum

class ActionType(Enum):
    """An enum to define the different types of actions that can be performed."""
    
    CLICK = 'CLICK'
    INFINITE_SCROLL = 'INFINITE_SCROLL'
    GET_LINK = 'GET_LINK'
    GET_ALL_LINKS = 'GET_ALL_LINKS'
    GET_TEXT = 'GET_TEXT'
    SET_TEXT = 'SET_TEXT'
    GOTO_URL = 'GOTO_URL'