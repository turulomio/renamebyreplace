from gettext import translation
from datetime import datetime
__version__ = '1.0.0'
__versiondatetime__=datetime(2026, 1, 11,7,39)
__versiondate__=__versiondatetime__.date()
from importlib.resources import files

try:
    t=translation('renamebyreplace', files('renamebyreplace') / 'locale')
    _=t.gettext
except:
    _=str

def epilog():
    return _("Developed by Mariano Muñoz 2018-{}").format(__versiondate__.year  )