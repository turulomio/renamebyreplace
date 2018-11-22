#!/usr/bin/python3
import argparse
import time
import colorama
import os
import subprocess
import gettext
from ttyrecgenerator import RecSession
import pkg_resources
gettext.install('recpermissions', pkg_resources.resource_filename('recpermissions', 'locale'))

#We change permissions for the howto
os.system("mkdir -p example")
os.system("touch example/MyFavoriteFilm 1.mkv")
os.system("touch example/MyFavoriteFilm 2.mkv")
os.system("touch example/MyFavoriteFilm 3.mkv")
os.chdir("example")

r=RecSession()
r.comment("# " + _("This is a video to show how to use 'renamebyreplace' command"))
r.comment("# " + _("We list files in a directory with permissions and owners"))
r.command("ls -la")

r.comment("# " + _("We want to rename files to MySecondFavoriteFilm in all files:"))
r.command("renamebyreplace --seach MyFavoriteFilm --replace MySecondFavoriteFilm")
r.comment("# " + _("We like the pretended output so we want to make the changes:"))
r.command("renamebyreplace --seach MyFavoriteFilm --replace MySecondFavoriteFilm --write")
r.comment("# " + _("That's all"))
time.sleep(30)
r.comment("# ")
#We remove example
os.chdir("..")
os.system("rm -Rf example")
