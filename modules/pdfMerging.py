#!/bin/python3

import os
from pypdf import PdfWriter
from natsort import natsorted

def pdfMerging_func(directory, template):
    print('\033[33m'+'Merging all the pdf files'+'\033[0m')
    merger = PdfWriter()
    listDirectory = natsorted(os.listdir(directory+'/.mde2pdfTmp/pdf-u'))
    lenDirectory = len(listDirectory)
    i = 0
    while i < lenDirectory:
        pdfMergingName = os.path.expanduser(os.path.join(directory+'/.mde2pdfTmp/pdf-u', listDirectory[i]))
        merger.append(pdfMergingName)
        i += 1
    merger.write(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf')
    merger.close()