__all__ = [
    '__version__',
    'CCraftVersion'
]

from packaging.version import Version
from platform import python_version

__version__ = "1.0.0a0"
__PythonMRV__ = "3.12.3"
CCraftVersion = Version(__version__)

if Version(python_version()) < Version(__PythonMRV__):
    raise RuntimeError(
        'CCraft ' + __version__ + ' requires minimum Python ' + __PythonMRV__ + '! ' +
        'Your\'s Python is ' + python_version() + '.'
    )
