from gettext import translation
from datetime import date
__version__ = '0.2.0'
__versiondate__=date(2026, 1, 11)
from importlib.resources import files

try:
    t=translation('renamebyreplace', files('renamebyreplace') / 'locale')
    _=t.gettext
except:
    _=str

def epilog():
    return _("Developed by Mariano Muñoz 2018-{}").format(__versiondate__.year  )