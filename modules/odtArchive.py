#!/bin/python3

import os
from shutil import make_archive

def odtArchiveCreate_func(directory, lmdeName):
    print('\033[33m'+'Creating odt archive'+'\033[0m')
    odtArchiveName = os.path.expanduser(os.path.join(directory, '.mde2pdfTmp/odt-c/'+lmdeName))
    odtArchiveDirectory = os.path.expanduser(os.path.join(directory, '.mde2pdfTmp/odt-u'))
    make_archive(odtArchiveName, 'zip', odtArchiveDirectory)
    os.rename(directory+'/.mde2pdfTmp/odt-c/'+lmdeName+'.zip', directory+'/.mde2pdfTmp/odt-c/'+lmdeName+'.odt')