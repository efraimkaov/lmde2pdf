#!/bin/python3

import os
from pypdf import PdfReader
from modules.manifestXml import manifestXml_func
from modules.manifestRdf import manifestRdf_func
from modules.stylesXml import stylesXml_func
from modules.contentXmlBilingual import contentXmlBilingual_func
from modules.odtArchive import odtArchiveCreate_func
from modules.odt2pdf import odt2pdfConvert_func
from modules.pdfMerging import pdfMerging_func

def lmdeNameBilingual_func(directory, lmdeName, lmdeFilesLenCount, installationDir, template, lang1, ctry1, lang2, ctry2):
    # Creating variables for leftHeader and rightHeader
    global pageLenMerged
    leftHeader = ''
    rightHeader = ''
    leftHeaderValidate = False
    rightHeaderValidate = False
    secondPage = ''
    defaultStyle = ''

    lmdeFilesLeftHeader = open(directory+'/'+lmdeName+'.lmde', 'r')
    leftHeaderAllLen = len(lmdeFilesLeftHeader.readlines())
    lmdeFilesLeftHeader.close()

    lmdeFilesLeftHeader = open(directory+'/'+lmdeName+'.lmde', 'r')
    if leftHeaderAllLen < 1:
        print('\033[31m'+'You must have at least 1 line in '+lmdeName+'.lmde'+'\033[0m')
        quit()
    leftHeaderAll = lmdeFilesLeftHeader.readlines()[0]
    leftHeaderVar = leftHeaderAll.split('(')[0]
    if leftHeaderVar == '[lh]' and ')' in leftHeaderAll:
        leftHeaderValidate = True
        leftHeader = leftHeaderAll.split('(')[1].split(')')[0]
    else:
        leftHeaderValidate = False
    lmdeFilesLeftHeader.close()

    if leftHeaderAllLen > 1:
        lmdeFilesRightHeader = open(directory+'/'+lmdeName+'.lmde', 'r')
        rightHeaderAll = lmdeFilesRightHeader.readlines()[1]
        rightHeaderVar = rightHeaderAll.split('(')[0]
        if rightHeaderVar == '[rh]' and ')' in rightHeaderAll:
            rightHeaderValidate = True
            rightHeader = rightHeaderAll.split('(')[1].split(')')[0]
        else:
            rightHeaderValidate = False
        lmdeFilesRightHeader.close()

    # Creating variables for defaultStyle, pageNumber and secondPage
    if leftHeaderValidate == True and rightHeaderValidate == True:
        if leftHeaderAllLen < 3:
            print('\033[31m'+'You must have at least 3 lines in '+lmdeName+'.lmde'+'\033[0m')
            quit()
        lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
        defaultStyleAll = lmdeFilesDefaultStyle.readlines()[2]
        defaultStyleVar = defaultStyleAll.split(' ')[0]
        if '#' == defaultStyleVar:
            defaultStyle = 'h1'
        elif '##' == defaultStyleVar:
            defaultStyle = 'h2'
        elif '###' == defaultStyleVar:
            defaultStyle = 'h3'
        elif '$' == defaultStyleVar:
            defaultStyle = 'p1'
        elif '$^' == defaultStyleVar:
            defaultStyle = 'p1-dc'
        elif '$$' == defaultStyleVar:
            defaultStyle = 'p2'
        elif '[png]' in defaultStyleVar:
            defaultStyle = 'i'
        elif '[toc]' in defaultStyleVar:
            defaultStyle = 'toch'
        else:
            lmdeFilesDefaultStyle.close()
            print('\033[31m'+'You have errors in '+lmdeName+'.lmde'+'\033[0m')
            quit()
        lmdeFilesDefaultStyle.close()

        if lmdeFilesLenCount == 0:
            pageNumber = 1
            secondPage = 'lp'
        else:
            pageNumber = pageLenMerged + 1

            if (pageNumber % 2) == 0:
                secondPage = 'rp'
            else:
                secondPage = 'lp'
    else:
        lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
        defaultStyleAll = lmdeFilesDefaultStyle.readlines()[0]
        defaultStyleVar = defaultStyleAll.split(' ')[0]
        if '#' == defaultStyleVar:
            defaultStyle = 'h1'
        elif '##' == defaultStyleVar:
            defaultStyle = 'h2'
        elif '###' == defaultStyleVar:
            defaultStyle = 'h3'
        elif '$' == defaultStyleVar:
            defaultStyle = 'p1'
        elif '$^' == defaultStyleVar:
            defaultStyle = 'p1-dc'
        elif '$$' == defaultStyleVar:
            defaultStyle = 'p2'
        elif '[png]' in defaultStyleVar:
            defaultStyle = 'i'
        elif '[toc]' in defaultStyleVar:
            defaultStyle = 'toch'
        else:
            lmdeFilesDefaultStyle.close()
            print('\033[31m'+'You have errors in '+lmdeName+'.lmde'+'\033[0m')
            quit()
        lmdeFilesDefaultStyle.close()

        if lmdeFilesLenCount == 0:
            pageNumber = 1
            secondPage = 'fp'
        else:
            pageNumber = pageLenMerged + 1
            secondPage = 'fp'

    # Generating manifest.xml
    manifestXml_func(directory)

    # Generating manifest.rdf
    manifestRdf_func(directory)

    # Generating styles.xml
    stylesXml_func(directory, installationDir, template, lang1, ctry1, lang2, ctry2, secondPage, leftHeader, rightHeader)

    # Generating content.xml
    contentXmlBilingual_func(directory, installationDir, template, pageNumber, defaultStyle, lmdeName, leftHeaderValidate, rightHeaderValidate)

    # Creating odt archive
    odtArchiveCreate_func(directory, lmdeName)

    # Converting odt to pdf
    odt2pdfConvert_func(directory, lmdeName)

    # Create pageNumberFile.txt for table of contents
    if leftHeaderValidate == True and rightHeaderValidate == True:
        if leftHeaderAllLen > 2:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[2]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 3:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[3]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 4:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[4]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 5:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[5]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()
    else:
        if leftHeaderAllLen > 0:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[0]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 1:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[1]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 2:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[2]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

        if leftHeaderAllLen > 3:
            pageNumberFile = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'a')
            lmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
            defaultStyleAll = lmdeFilesDefaultStyle.readlines()[3]
            defaultStyleVar = defaultStyleAll.split(' ')[0]
            if '##' == defaultStyleVar:
                pageNumberFile.write(defaultStyleAll.replace('\n', '')+' [(#'+str(pageNumber)+'#)]\n')
            lmdeFilesDefaultStyle.close()
            pageNumberFile.close()

    # Merging all the pdf files
    pdfMerging_func(directory, template)

    # Get page count for the last merged pdf
    readerMerged = PdfReader(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf')
    pageLenMerged = len(readerMerged.pages)

    # Removing temporary files
    os.remove(directory+'/.mde2pdfTmp/odt-u/META-INF/manifest.xml')
    os.remove(directory+'/.mde2pdfTmp/odt-u/content.xml')
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.remove(directory+'/.mde2pdfTmp/odt-u/manifest.rdf')