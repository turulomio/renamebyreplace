from argparse import ArgumentParser
from . import _, epilog
from os import listdir, getcwd, rename

def maxlenarr(arr):
    r=0
    for item in arr:
        if len(item)>r:
            r=len(item)
    return r

## @param parameters is a list. For example ['--search',]
def main():
    parser=ArgumentParser(_('Rename files searching substrings in filenames' ), epilog=epilog())
    parser.add_argument('--search', help=_('String to search'), action='store', required=True)
    parser.add_argument('--replace', help=_('String to replace'), action='store', required=True)
    parser.add_argument('--write', help=_('Renames the files'), action='store_true', default=False)
    parser.add_argument('--undo', help=_('Undo replace command'), action='store_true', default=False)
    args=parser.parse_args()
    renamebyreplace(args.search, args.replace, args.write, args.undo)


def renamebyreplace(search, replace, write, undo):

    arrFrom=[]
    arrTo=[]
    files = listdir(getcwd())

    if undo==True:
        tmp=search
        search=replace
        replace=tmp

    for file in files:
        if file.find(search)!=-1:
            arrFrom.append(file)
            arrTo.append(file.replace(search,replace))

    maxarr=maxlenarr(arrFrom)
    for i in range(len(arrFrom)):
        print ("{} ==> {}".format(arrFrom[i].ljust(maxarr),arrTo[i]))
        if write==True:
            rename(arrFrom[i],arrTo[i])

    if write==True:
        print (_("Changes have been made ;)."))
