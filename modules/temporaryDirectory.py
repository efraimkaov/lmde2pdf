#!/bin/python3

import os
import shutil

def temporaryDirectoryCreate_func(directory):
    print('\033[33m'+'Creating temporary directories'+'\033[0m')
    os.mkdir(os.path.join(directory, '.mde2pdfTmp'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/odt-u'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/odt-u/META-INF'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/odt-c'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/pdf-u'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/pdf-c'))
    os.mkdir(os.path.join(directory, '.mde2pdfTmp/pn'))

def temporaryDirectoryRemove_func(directory):
    if os.path.exists(directory+'/.mde2pdfTmp') == True:
        print('\033[31m'+'Removing temporary directories'+'\033[0m')
        shutil.rmtree(directory+'/.mde2pdfTmp')