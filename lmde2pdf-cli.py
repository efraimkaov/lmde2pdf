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
language = ''
country = ''
directory = ''

if args.show == True:
    templateCfg = open(installationDir+'/templates/template.cfg', 'r')
    print(templateCfg.read())
    templateCfg.close()
    quit()

if args.info != None:
    templateName = args.info
    detailsTxt = open(installationDir+'/templates/'+templateName+'/details.txt', 'r')
    print(detailsTxt.read())
    detailsTxt.close()
    quit()

if args.codes == True:
    languagesCode = open(installationDir+'/templates/'+'languages-code.txt', 'r')
    print(languagesCode.read())
    languagesCode.close()
    quit()

if args.template != None and args.lang1 != None and args.lang2 == None and args.directory != None:
    templateLayout = args.template
    langFirst = args.lang1
    templateType = open(installationDir+'/templates/'+templateLayout+'/details.txt', 'r')
    templateTypeRegular = templateType.readlines()[0]
    templateType.close
    if 'regular' in templateTypeRegular:
        template = templateLayout
        directory = args.directory
        language1 = args.lang1
        lang1 = language1.split('-')[0]
        ctry1 = language1.split('-')[1]
        lang2 = ''
        ctry2 = ''
    else:
        print('\033[31m'+'Wrong template or arguments for this template!'+'\033[0m')
        quit()
elif args.template != None and args.lang1 != None and args.lang2 != None and args.directory != None:
    templateLayout = args.template
    langFirst = args.lang1
    templateType = open(installationDir+'/templates/'+templateLayout+'/details.txt', 'r')
    templateTypeRegular = templateType.readlines()[0]
    templateType.close
    if 'bilingual' in templateTypeRegular:
        template = templateLayout
        directory = args.directory
        language1 = args.lang1
        language2 = args.lang2
        lang1 = language1.split('-')[0]
        ctry1 = language1.split('-')[1]
        lang2 = language2.split('-')[0]
        ctry2 = language2.split('-')[1]
    else:
        print('\033[31m'+'\033[31m'+'Wrong template or arguments for this template!'+'\033[0m'+'\033[0m')
        quit()

lmde2pdf_func(templateTypeRegular, directory, installationDir, lang1, ctry1, lang2, ctry2, templateLayout, template)