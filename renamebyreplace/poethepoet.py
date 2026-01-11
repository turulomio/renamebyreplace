from renamebyreplace import _, __version__
from os import system


def release():
    print(_("New Release:"))
    print (_("  * Create a new issue and its branch in Github"))
    print (_("  * Change to this branch pasting suggested code in Github"))
    print(_("  * Change version and date in __init__.py"))
    print("  * poe translate")
    print("  * mcedit locale/es.po")
    print("  * poe translate")
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
    print(_("You need ttyrecgenerator installed to generate videos"))
    # chdir("doc/ttyrec")
    # system("ttyrecgenerator --output renamebyreplace_howto_es 'python3 howto.py' --lc_all es_ES.UTF-8")
    # system("ttyrecgenerator --output renamebyreplace_howto_en 'python3 howto.py' --lc_all C")
    # chdir("../..")


    # _=gettext.gettext#To avoid warnings
    # #!/usr/bin/python3
    # import argparse
    # import time
    # import colorama
    # import os
    # import subprocess
    # import gettext
    # from ttyrecgenerator import RecSession
    # import pkg_resources
    # gettext.install('renamebyreplace', pkg_resources.resource_filename('renamebyreplace', 'locale'))

    # #We change permissions for the howto
    # system("mkdir -p example")
    # system("touch 'example/MyFavoriteFilm 1.mkv'")
    # system("touch 'example/MyFavoriteFilm 2.mkv'")
    # system("touch 'example/MyFavoriteFilm 3.mkv'")
    # chdir("example")

    # r=RecSession()
    # r.comment("# " + _("This is a video to show how to use 'renamebyreplace' command"))
    # r.comment("# " + _("We list files in our example directory"))
    # r.command("ls -la")

    # r.comment("# " + _("We want to rename files to MySecondFavoriteFilm in all files:"))
    # r.command("renamebyreplace --search MyFavoriteFilm --replace MySecondFavoriteFilm")
    # r.comment("# " + _("We like the pretended output so we want to make the changes:"))
    # r.command("renamebyreplace --search MyFavoriteFilm --replace MySecondFavoriteFilm --write")
    # r.comment("# " + _("We check the result:"))
    # r.command("ls -la")
    # r.comment("# " + _("That's all"))
    # time.sleep(20)
    # r.comment("# ")
    # #We remove example
    # chdir("..")
    # system("rm -Rf example")
