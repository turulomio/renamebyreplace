from setuptools import setup, Command
import datetime
import gettext
import os
import platform
import site

gettext.install('renamebyreplace', 'renamebyreplace/locale')

class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
        os.system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
        os.system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
        os.system("rm -Rf build")
        os.chdir("doc")
        os.system("doxygen Doxyfile")
        os.system("rsync -avzP -e 'ssh -l turulomio' html/ frs.sourceforge.net:/home/users/t/tu/turulomio/userweb/htdocs/doxygen/renamebyreplace/ --delete-after")
        os.chdir("..")

class Procedure(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(_("New Release:"))
        print(_("  * Change version and date in version.py"))
        print(_("  * Edit Changelog in README"))
        print("  * python setup.py doc")
        print("  * mcedit locale/es.po")
        print("  * python setup.py doc")
        print("  * python setup.py install")
        print("  * python setup.py doxygen")
        print("  * mcedit doc/ttyrec/howto.py")
        print("  * python setup.py video" + ". " + _("If changed restart from first python setup.py doc"))
        print("  * git commit -a -m 'renamebyreplace-{}'".format(__version__))
        print("  * git push")
        print(_("  * Make a new tag in github"))
        print("  * python setup.py sdist upload -r pypi")
        print(_("  * Create a new gentoo ebuild with the new version"))
        print(_("  * Upload to portage repository")) 

class Uninstall(Command):
    description = "Uninstall installed files with install"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if platform.system()=="Linux":
            os.system("rm -Rf {}/renamebyreplace*".format(site.getsitepackages()[0]))
            os.system("rm /usr/bin/renamebyreplace")
            os.system("rm /usr/share/man/man1/renamebyreplace.1")
            os.system("rm /usr/share/man/fr/man1/renamebyreplace.1")
            os.system("rm /usr/share/man/es/man1/renamebyreplace.1")
        else:
            print(site.getsitepackages())
            for file in os.listdir(site.getsitepackages()[1]):#site packages
                path=site.getsitepackages()[1]+"\\"+ file
                if file.find("renamebyreplace")!=-1:
                    shutil.rmtree(path)
                    print(path,  "Erased")
            for file in os.listdir(site.getsitepackages()[0]+"\\Scripts\\"):#Scripts
                path=site.getsitepackages()[0]+"\\scripts\\"+ file
                if file.find("renamebyreplace")!=-1:
                    os.remove(path)
                    print(path,  "Erased")

class Doc(Command):
    description = "Update man pages and translations"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        #es
        os.system("xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o locale/renamebyreplace.pot *.py renamebyreplace/*.py doc/ttyrec/*.py")
        os.system("msgmerge -N --no-wrap -U locale/es.po locale/renamebyreplace.pot")
        os.system("msgmerge -N --no-wrap -U locale/fr.po locale/renamebyreplace.pot")
        os.system("msgfmt -cv -o renamebyreplace/locale/es/LC_MESSAGES/renamebyreplace.mo locale/es.po")
        os.system("msgfmt -cv -o renamebyreplace/locale/fr/LC_MESSAGES/renamebyreplace.mo locale/fr.po")

        for language in ["en", "es", "fr"]:
            self.mangenerator(language)

    def mangenerator(self, language):
        """
            Create man pages for parameter language
        """
        from mangenerator import Man
        if language=="en":
            lang1=gettext.install('renamebyreplace', 'badlocale')
            man=Man("man/man1/renamebyreplace")
        else:
            lang1=gettext.translation('renamebyreplace', 'renamebyreplace/locale', languages=[language])
            lang1.install()
            man=Man("man/{}/man1/renamebyreplace".format(language))
        print("  - DESCRIPTION in {} is {}".format(language, _("DESCRIPTION")))

        man.setMetadata("renamebyreplace",  1,   datetime.date.today(), "Mariano Muñoz", _("Rename files replacing subtrings in filename"))
        man.setSynopsis("""usage: renamebyreplace [-h] [--search SEARCH] [--replace REPLACE] [--write] [--undo]""")
        man.header(_("DESCRIPTION"), 1)
        man.paragraph(_("This app has the following mandatory parameters:"), 1)
        man.paragraph("--search", 2, True)
        man.paragraph(_("Search this substring in the filename"), 3)
        man.paragraph("--replace", 2, True)
        man.paragraph(_("Replace search substring with this substring"), 3)
        man.paragraph("--undo", 2, True)
        man.paragraph(_("Uses the --search argument as the --replace one and the --replace argument as the --search one"))
        man.paragraph("If you want to write changes in filesystem you must add --write parameter", 2)
        man.header(_("EXAMPLES"), 1)
        man.paragraph(_("Pretend example"), 2, True)
        man.paragraph("renamebyreplace --search ABCD --replace Abcd", 3)
        man.paragraph(_("This comand pretends the renaming"), 3)
        man.paragraph(_("Write Example"), 2, True)
        man.paragraph("renamebyreplace --search ABCD --replace Abcd --writes", 3)
        man.paragraph(_("This comand makes the renaming"), 3)
        man.save()

class Video(Command):
    description = "Create video/GIF from console ouput"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(_("You need ttyrecgenerator installed to generate videos"))
        os.chdir("doc/ttyrec")
        os.system("ttyrecgenerator --output renamebyreplace_howto_es 'python3 howto.py' --lc_all es_ES.UTF-8")
        os.system("ttyrecgenerator --output renamebyreplace_howto_en 'python3 howto.py' --lc_all C")
        os.chdir("../..")

    ########################################################################


## Version of modele captured from version to avoid problems with package dependencies
__version__= None
with open('renamebyreplace/version.py', encoding='utf-8') as f:
    for line in f.readlines():
        if line.find("__version__ =")!=-1:
            __version__=line.split("'")[1]


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

if platform.system()=="Linux":
    data_files=[('/usr/share/man/man1/', ['man/man1/renamebyreplace.1']),
                ('/usr/share/man/es/man1/', ['man/es/man1/renamebyreplace.1']),
                ('/usr/share/man/fr/man1/', ['man/fr/man1/renamebyreplace.1']),
               ]
else:
    data_files=[]

setup(name='renamebyreplace',
    version=__version__,
    description='Rename files searching substrings in filenames',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: System Administrators',
                 'Topic :: System :: Systems Administration',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 3',
                ],
    keywords='rename replace filenames',
    url='https://github.com/Turulomio/renamebyreplace',
    author='Turulomio',
    author_email='turulomio@yahoo.es',
    license='GPL-3',
    packages=['renamebyreplace'],
    entry_points = {'console_scripts': ['renamebyreplace=renamebyreplace.core:main',
                                       ],
                   },
    install_requires=['colorama','setuptools'],
    data_files=data_files,
    cmdclass={ 'doxygen': Doxygen,
               'doc': Doc,
               'uninstall': Uninstall,
               'video': Video,
               'procedure': Procedure,
             },
    zip_safe=False,
    include_package_data=True
    )

_=gettext.gettext#To avoid warnings
