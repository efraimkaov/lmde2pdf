#!/bin/python3

import os
import subprocess

def odt2pdfConvert_func(directory, lmdeName):
    print('\033[33m'+'Converting odt to pdf'+'\033[0m')
    odt2pdfName = os.path.expanduser(os.path.join(directory, '.mde2pdfTmp/odt-c/'+lmdeName+'.odt'))
    odt2pdfDirectory = os.path.expanduser(os.path.join(directory, '.mde2pdfTmp/pdf-u'))
    subprocess.call(['soffice', '--headless', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', odt2pdfDirectory, odt2pdfName])