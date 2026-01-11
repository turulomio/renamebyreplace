from gettext import translation
from datetime import date
__version__ = '0.2.0'
__versiondate__=date(2019, 2, 1)
from importlib.resources import files

try:
    t=translation('renamebyreplace', files('renamebyreplace') / 'locale')
    _=t.gettext
except:
    _=str