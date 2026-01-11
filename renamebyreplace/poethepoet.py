from renamebyreplace import _, __version__
from os import system, chdir, remove
from shutil import which


def release():
    print(_("New Release:"))
    print (_("  * Create a new issue and its branch in Github"))
    print (_("  * Change to this branch pasting suggested code in Github"))
    print(_("  * Change version and date in __init__.py and in pyproject.ml"))
    print("  * poe translate")
    print("  * mcedit locale/es.po")
    print("  * poe translate")
    print("  * poe video")
    print("  * poe coverage")
    print("  * git commit -a -m 'renamebyreplace-{}'".format(__version__))
    print("  * git push")
    print(_("  * Make a pull request to main branch"))
    print(_("  * Make a new tag in github"))
    print("  * poetry publish")
    print(_("  * Create a new gentoo ebuild with the new version and install it"))
    print(_("  * Upload to portage repository")) 


def translate():
        #es
        system("xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o renamebyreplace/locale/renamebyreplace.pot renamebyreplace/*.py")
        system("msgmerge -N --no-wrap -U renamebyreplace/locale/es.po renamebyreplace/locale/renamebyreplace.pot")
        system("msgmerge -N --no-wrap -U renamebyreplace/locale/fr.po renamebyreplace/locale/renamebyreplace.pot")
        system("msgfmt -cv -o renamebyreplace/locale/es/LC_MESSAGES/renamebyreplace.mo renamebyreplace/locale/es.po")
        system("msgfmt -cv -o renamebyreplace/locale/fr/LC_MESSAGES/renamebyreplace.mo renamebyreplace/locale/fr.po")

def coverage():
    system("coverage run -m pytest && coverage report && coverage html")

def video():
    # Comprobaciones
    vhs=which("vhs")
    if vhs is None: 
        print(_("vhs tool is needed. Look at https://github.com/charmbracelet/vhs"))
        exit(1)

    chdir("doc")
    system(f"{vhs} command.tape")
    system(f"{vhs} howto.tape")
    system("rm *.mp4")

