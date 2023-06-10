#!/bin/python3

import os
import argparse
from modules.lmde2pdfMain import lmde2pdf_func

# program arguments
installationDir = os.path.dirname(__file__)
programVersionRead = open(installationDir+'/version', 'r')
programVersion = programVersionRead.read()
programVersionRead.close()
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='%(prog)s '+programVersion)
parser.add_argument('-s', '--show', help='list all templates and exit', action='store_true')
parser.add_argument('-i', '--info', help='display template details and exit')
parser.add_argument('-c', '--codes', help='display languages code and exit', action='store_true')
parser.add_argument('-t', '--template', help='select the template')
parser.add_argument('-l1', '--lang1', help='select the first language code for hyphenation')
parser.add_argument('-l2', '--lang2', help='select the second language code for hyphenation')
parser.add_argument('-d', '--directory', help='select the full path for the input directory')
args = parser.parse_args()

template = ''
templateType = ''
lang1 = ''
ctry1 = ''
lang2 = ''
ctry2 = ''
directory = ''

if args.show == True:
    templateCfg = open(installationDir+'/templates/template.cfg', 'r')
    print(templateCfg.read())
    templateCfg.close()
    quit()

if args.info != None:
    template = args.info
    templateCheckOpen = open(installationDir+'/templates/template.cfg', 'r')
    templateCheck = templateCheckOpen.read()
    templateCheckOpen.close()
    if template+'\n' in templateCheck:
        detailsTxt = open(installationDir+'/templates/'+template+'/details.txt', 'r')
        print(detailsTxt.read())
        detailsTxt.close()
        quit()
    else:
        print('\033[31m'+'Wrong template!'+'\033[0m')
        quit()

if args.codes == True:
    languagesCode = open(installationDir+'/templates/'+'languages-code.txt', 'r')
    print(languagesCode.read())
    languagesCode.close()
    quit()

if args.template != None:
    template = args.template
    templateCheckOpen = open(installationDir+'/templates/template.cfg', 'r')
    templateCheck = templateCheckOpen.read()
    templateCheckOpen.close()
    if template+'\n' in templateCheck:
        templateOpen = open(installationDir+'/templates/'+template+'/details.txt', 'r')
        templateType = templateOpen.readlines()[0]
        templateOpen.close
    else:
        print('\033[31m'+'Wrong template!'+'\033[0m')
        quit()

if args.lang1 != None:
    language1 = args.lang1
    language1CheckOpen = open(installationDir+'/templates/'+'languages-code.txt', 'r')
    language1Check = language1CheckOpen.read()
    language1CheckOpen.close()
    if language1+'\n' in language1Check:
        lang1 = language1.split('-')[0]
        ctry1 = language1.split('-')[1]
    else:
        print('\033[31m'+'Wrong language1!'+'\033[0m')
        quit()

if args.lang2 != None:
    language2 = args.lang2
    language2CheckOpen = open(installationDir+'/templates/'+'languages-code.txt', 'r')
    language2Check = language2CheckOpen.read()
    language2CheckOpen.close()
    if language2+'\n' in language1Check:
        lang2 = language2.split('-')[0]
        ctry2 = language2.split('-')[1]
    else:
        print('\033[31m'+'Wrong language2!'+'\033[0m')
        quit()

if args.directory != None:
    directory = args.directory

guiCheck = False

lmde2pdf_func(guiCheck, installationDir, template, templateType, lang1, ctry1, lang2, ctry2, directory)