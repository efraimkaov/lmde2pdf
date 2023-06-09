#!/bin/python3

import os

def stylesXml_func(directory, installationDir, template, lang1, ctry1, lang2, ctry2, secondPage, leftHeader, rightHeader):
    print('\033[33m'+'Generating styles.xml'+'\033[0m')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'a')
    stylesXml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    stylesXml.write('<office:document-styles xmlns:officeooo="http://openoffice.org/2009/office" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:rpt="http://openoffice.org/2005/report" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xhtml="http://www.w3.org/1999/xhtml" office:version="1.3">\n')
    stylesXml.close()

    stylesXmlTemplate = open(installationDir+'/templates/'+template+'/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'a')
    for line in stylesXmlTemplate.readlines():
        stylesXml.write(line)
    stylesXml.close()
    stylesXmlTemplate.close()

    stylesXmlTemplate = open(installationDir+'/templates/'+template+'/automatic-styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'a')
    for line in stylesXmlTemplate.readlines():
        stylesXml.write(line)
    stylesXml.close()
    stylesXmlTemplate.close()

    stylesXmlTemplate = open(installationDir+'/templates/'+template+'/master-styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'a')
    for line in stylesXmlTemplate.readlines():
        stylesXml.write(line)
    stylesXml.close()
    stylesXmlTemplate.close()

    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'a')
    stylesXml.write('</office:document-styles>')
    stylesXml.close()

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-lang1.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#lang1#', lang1))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-lang1.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-ctry1.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#ctry1#', ctry1))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-ctry1.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-lang2.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#lang2#', lang2))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-lang2.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-ctry2.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#ctry2#', ctry2))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-ctry2.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-secondPage.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#secondPage#', secondPage))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-secondPage.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-leftHeader.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#leftHeader#', leftHeader))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-leftHeader.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')

    stylesXmlTemplate = open(directory+'/.mde2pdfTmp/odt-u/styles.xml', 'r')
    stylesXml = open(directory+'/.mde2pdfTmp/odt-u/styles-rightHeader.xml', 'a')
    for line in stylesXmlTemplate:
        stylesXml.write(line.replace('#rightHeader#', rightHeader))
    stylesXml.close()
    stylesXmlTemplate.close()
    os.remove(directory+'/.mde2pdfTmp/odt-u/styles.xml')
    os.rename(directory+'/.mde2pdfTmp/odt-u/styles-rightHeader.xml', directory+'/.mde2pdfTmp/odt-u/styles.xml')