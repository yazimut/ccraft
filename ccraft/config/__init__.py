# from config import *
# place here module names that would be accessed through NAME
__all__ = [
    'version'
    'config',
]

# import config
# place here all names that would be accessed through config.NAME
from .version import *
from .config import *
