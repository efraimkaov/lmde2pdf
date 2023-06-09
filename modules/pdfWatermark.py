#!/bin/python3

import shutil
from pypdf import PdfWriter, PdfReader, Transformation

def pdfWatermark_func(directory, template, installationDir):
    print('\033[33m'+'Generating the final pdf'+'\033[0m')
    templateBorder = open(installationDir+'/templates/'+template+'/details.txt', 'r')
    templateBorderYes = templateBorder.readlines()[1]
    if 'yes' in templateBorderYes:
        print('\033[33m'+'Adding border to the final pdf, this may take a whike!'+'\033[0m')
        reader = PdfReader(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf')
        page_indices = range(len(reader.pages))
        writer = PdfWriter()
        watermark_page = PdfReader(installationDir+'/templates/'+template+'/border.pdf').pages[0]
        for index in page_indices:
            content_page = reader.pages[index]
            content_page.merge_transformed_page(watermark_page, Transformation(), over=False)
            writer.add_page(content_page)
        with open(directory+'/'+template+'-border.pdf', 'wb') as fp:
            writer.write(fp)
    else:
        shutil.copyfile(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf', directory+'/'+template+'.pdf')
    templateBorder.close()