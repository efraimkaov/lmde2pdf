#!/bin/python3

import os
import shutil
from natsort import natsorted
from pypdf import PdfWriter
from modules.temporaryDirectory import temporaryDirectoryCreate_func
from modules.temporaryDirectory import temporaryDirectoryRemove_func
from modules.lmdeName import lmdeName_func
from modules.lmdeNameBilingual import lmdeNameBilingual_func
from modules.pdfSplitting import pdfSplitting_func
from modules.pdfWatermark import pdfWatermark_func

def lmde2pdf_func(templateTypeRegular, directory, installationDir, lang1, ctry1, lang2, ctry2, templateLayout, template):
    if 'regular' in templateTypeRegular:

        # Getting the lmde files from given location
        listDirectory = natsorted(os.listdir(directory))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        lmdeFilesString = ''
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                lmdeListName = listDirectory[lenDirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            lenDirectoryCount += 1
        lmdeFilesList = list(lmdeFilesString.split('#&#'))
        lmdeFilesLen = len(lmdeFilesList) - 1
        if lmdeFilesLen < 1:
            print('\033[31m'+'No lmde files found in '+directory+'\033[0m')
            quit()

        # Removing temporary directories
        temporaryDirectoryRemove_func(directory)

        # Creating temporary directories
        temporaryDirectoryCreate_func(directory)

        pageNumber = 0
        odtName = ''
        lmdeName = ''
        lmdeFilesLenCount = 0

        while lmdeFilesLenCount < lmdeFilesLen:
            lmdeName = lmdeFilesList[lmdeFilesLenCount]

            # Converting lmde files for regualr template to pdf
            lmdeName_func(directory, lmdeName, lmdeFilesLenCount, installationDir, template, lang1, ctry1, lang2, ctry2)

            lmdeFilesLenCount += 1

        # Generating the final pdf
        pdfWatermark_func(directory, template, installationDir)
    else:

        # Checking for lmde files in given location
        listDirectory = natsorted(os.listdir(directory))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        lmdeFilesString = ''
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                lmdeListName = listDirectory[lenDirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            lenDirectoryCount += 1
        lmdeFilesList = list(lmdeFilesString.split('#&#'))
        lmdeFilesLen = len(lmdeFilesList) - 1

        # Restricting lmde files in given location
        if lmdeFilesLen > 0:
            print('\033[31m'+'For bilingual templates lmde files are only allowed in bilingual1 and bilingual2 subfolders from '+directory+'\033[0m')
            quit()

        # Getting the lmde files from bilingual1
        listBilingual1Directory = natsorted(os.listdir(directory+'/bilingual1'))
        lenDirectory = len(listBilingual1Directory)
        listBilingual1DirectoryCount = 0
        lmdeFilesString = ''
        while listBilingual1DirectoryCount < lenDirectory:
            if '.lmde' in listBilingual1Directory[listBilingual1DirectoryCount]:
                lmdeList = listBilingual1Directory[listBilingual1DirectoryCount]
                lmdeListName = listBilingual1Directory[listBilingual1DirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            listBilingual1DirectoryCount += 1
        lmdeFilesBilingual1List = list(lmdeFilesString.split('#&#'))
        lmdeFilesBilingual1Len = len(lmdeFilesBilingual1List) - 1

        # Getting the lmde files from bilingual2
        listBilingual2Directory = natsorted(os.listdir(directory+'/bilingual2'))
        lenDirectory = len(listBilingual2Directory)
        listBilingual2DirectoryCount = 0
        lmdeFilesString = ''
        while listBilingual2DirectoryCount < lenDirectory:
            if '.lmde' in listBilingual2Directory[listBilingual2DirectoryCount]:
                lmdeList = listBilingual2Directory[listBilingual2DirectoryCount]
                lmdeListName = listBilingual2Directory[listBilingual2DirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            listBilingual2DirectoryCount += 1
        lmdeFilesBilingual2List = list(lmdeFilesString.split('#&#'))
        lmdeFilesBilingual2Len = len(lmdeFilesBilingual2List) - 1

        # Checking if exist lmde files in bilingual1 and bilingual2
        if lmdeFilesBilingual1Len < 1 or lmdeFilesBilingual2Len < 1:
            print('\033[31m'+'No lmde files found in bilingual1 or bilingual2 subfolders from '+directory+'\033[0m')
            quit()

        # Checking if are the same numbers of lmde file in bilingual1 and bilingual2
        if lmdeFilesBilingual1Len != lmdeFilesBilingual2Len:
            print('\033[31m'+'The lmde files from bilingual1 and bilingual2 subfolders must be the same amount!'+'\033[0m')
            quit()

        # Comparing lines for lmde files from bilingual1 and bilingual2
        compareCount = 0
        while compareCount < lmdeFilesBilingual1Len:
            lmdeNameBilingual1 = lmdeFilesBilingual1List[compareCount]
            lmdeNameBilingual1Open = open(directory+'/bilingual1/'+lmdeNameBilingual1+'.lmde', 'r')
            lmdeNameBilingual1Len = len(lmdeNameBilingual1Open.readlines())
            lmdeNameBilingual1Open.close()

            lmdeNameBilingual2 = lmdeFilesBilingual2List[compareCount]
            lmdeNameBilingual2Open = open(directory+'/bilingual2/'+lmdeNameBilingual2+'.lmde', 'r')
            lmdeNameBilingual2Len = len(lmdeNameBilingual2Open.readlines())
            lmdeNameBilingual2Open.close()

            if lmdeNameBilingual1Len != lmdeNameBilingual2Len:
                print('\033[31m'+'The lmde files from bilingual1 and bilingual2 subfolders must have the same amount of lines!'+'\033[0m')
                quit()

            compareCount += 1

        # Combining lmde files from bilingual1 and bilingual2
        print('\033[33m'+'Combining lmde files from bilingual1 and bilingual2'+'\033[0m')
        compareCount = 0
        while compareCount < lmdeFilesBilingual1Len:
            lmdeNameBilingual1 = lmdeFilesBilingual1List[compareCount]
            lmdeNameBilingual2 = lmdeFilesBilingual2List[compareCount]

            lmdeNameBilingual1Open = open(directory+'/bilingual1/'+lmdeNameBilingual1+'.lmde', 'r')
            lmdeNameBilingual1Len = len(lmdeNameBilingual1Open.readlines())
            lmdeNameBilingual1Open.close()

            compareLineCount = 0
            while compareLineCount < lmdeNameBilingual1Len:
                lmdeNameBilingual1Open = open(directory+'/bilingual1/'+lmdeNameBilingual1+'.lmde', 'r')
                lmdeNameBilingual1All = lmdeNameBilingual1Open.readlines()[compareLineCount]
                lmdeNameBilingual2Open = open(directory+'/bilingual2/'+lmdeNameBilingual2+'.lmde', 'r')
                lmdeNameBilingual2All = lmdeNameBilingual2Open.readlines()[compareLineCount]

                lmdeNameBilingualOpen = open(directory+'/'+lmdeNameBilingual1+'.lmde', 'a')
                lmdeNameBilingualOpen.write(lmdeNameBilingual1All)
                lmdeNameBilingualOpen.write(lmdeNameBilingual2All)
                lmdeNameBilingualOpen.close()
                compareLineCount += 1

            lmdeNameBilingual2Open.close()
            lmdeNameBilingual1Open.close()
            compareCount += 1

        # Getting the lmde files from given location
        listDirectory = natsorted(os.listdir(directory))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        lmdeFilesString = ''
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                lmdeListName = listDirectory[lenDirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            lenDirectoryCount += 1
        lmdeFilesList = list(lmdeFilesString.split('#&#'))
        lmdeFilesLen = len(lmdeFilesList) - 1
        if lmdeFilesLen < 1:
            print('\033[31m'+'No combined lmde files found in '+directory+'\033[0m')
            quit()

        # Removing temporary directories
        temporaryDirectoryRemove_func(directory)

        # Creating temporary directories
        temporaryDirectoryCreate_func(directory)

        pageNumber = 0
        odtName = ''
        lmdeName = ''
        lmdeFilesLenCount = 0

        while lmdeFilesLenCount < lmdeFilesLen:
            lmdeName = lmdeFilesList[lmdeFilesLenCount]

            # Converting lmde files for bilingual template to pdf
            lmdeNameBilingual_func(directory, lmdeName, lmdeFilesLenCount, installationDir, template, lang1, ctry1, lang2, ctry2)

            lmdeFilesLenCount += 1

        # Check for front template
        templateFront = open(installationDir+'/templates/'+templateLayout+'/details.txt', 'r')
        templateFrontCheck = templateFront.readlines()[2]
        templateFrontName = template
        templateFront.close

        # Splitting bilingual pdf file in half
        if 'front' in templateFrontCheck:
            if 'no' not in templateFrontCheck:
                pdfSplitting_func(directory, templateFrontName)
                template = templateFrontCheck.split('"')[1]

        # Removing bilingual separate pdf files
        print('\033[31m'+'Removing bilingual separate pdf files'+'\033[0m')
        listDirectory = natsorted(os.listdir(directory+'/.mde2pdfTmp/pdf-u'))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        while lenDirectoryCount < lenDirectory:
            if '.pdf' in listDirectory[lenDirectoryCount]:
                pdfList = listDirectory[lenDirectoryCount]
                os.remove(directory+'/.mde2pdfTmp/pdf-u/'+pdfList)
            lenDirectoryCount += 1

        # Removing lmde files from given location
        print('\033[31m'+'Removing combined lmde files from '+directory+'\033[0m')
        listDirectory = natsorted(os.listdir(directory))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                os.remove(directory+'/'+lmdeList)
            lenDirectoryCount += 1

        # Getting the lmde files from front
        listDirectory = natsorted(os.listdir(directory+'/front'))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        lmdeFilesString = ''
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                shutil.copyfile(directory+'/front/'+lmdeList, directory+'/'+lmdeList)
                lmdeListName = listDirectory[lenDirectoryCount].replace('.lmde', '')
                lmdeFilesString += lmdeListName+'#&#'
            lenDirectoryCount += 1
        lmdeFilesList = list(lmdeFilesString.split('#&#'))
        lmdeFilesLen = len(lmdeFilesList) - 1
        if lmdeFilesLen > 0:
            #print('\033[31m'+'No lmde files found in '+directory+'/front'+'\033[0m')
            #quit()

            pageNumber = 0
            odtName = ''
            lmdeName = ''
            lmdeFilesLenCount = 0

            while lmdeFilesLenCount < lmdeFilesLen:
                lmdeName = lmdeFilesList[lmdeFilesLenCount]

                # Converting lmde files for regualr template to pdf
                lmdeName_func(directory, lmdeName, lmdeFilesLenCount, installationDir, template, lang1, ctry1, lang2, ctry2)

                lmdeFilesLenCount += 1

            os.remove(directory+'/.mde2pdfTmp/pdf-c/'+templateFrontName+'.pdf')
            merger = PdfWriter()
            for pdf in [directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf', directory+'/.mde2pdfTmp/pdf-c/'+templateFrontName+'-half.pdf']:
                merger.append(pdf)
            merger.write(directory+'/.mde2pdfTmp/pdf-c/'+templateFrontName+'.pdf')
            merger.close()
            
            template = templateFrontName

            # Generating the final pdf
            pdfWatermark_func(directory, template, installationDir)

        template = templateFrontName

        # Removing lmde files from given location
        print('\033[31m'+'Removing front lmde files from '+directory+'\033[0m')
        listDirectory = natsorted(os.listdir(directory))
        lenDirectory = len(listDirectory)
        lenDirectoryCount = 0
        while lenDirectoryCount < lenDirectory:
            if '.lmde' in listDirectory[lenDirectoryCount]:
                lmdeList = listDirectory[lenDirectoryCount]
                os.remove(directory+'/'+lmdeList)
            lenDirectoryCount += 1

    # Removing temporary directories
    temporaryDirectoryRemove_func(directory)

    # Printing All done!
    print('\033[32m'+'All done!'+'\033[0m')