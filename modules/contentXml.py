#!/bin/python3

from modules.lmdeTags import lmdeTags_func

def contentXml_func(directory, pageNumber, defaultStyle, lmdeName, leftHeaderValidate, rightHeaderValidate):
    print('\033[33m'+'Generating content.xml'+'\033[0m')
    contentXml = open(directory+'/.mde2pdfTmp/odt-u/content.xml', 'a')
    contentXml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    contentXml.write('<office:document-content xmlns:officeooo="http://openoffice.org/2009/office" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" office:version="1.3">\n')
    contentXml.write('<office:automatic-styles>\n')

    contentXml.write('<style:style style:name="P1" style:family="paragraph" style:parent-style-name="'+defaultStyle+'" style:master-page-name="fp">\n')
    contentXml.write('<style:paragraph-properties style:page-number="'+str(pageNumber)+'"/>\n')
    contentXml.write('</style:style>\n')
    contentXml.write('<style:style style:name="fr1" style:family="graphic" style:parent-style-name="Graphics">\n')
    contentXml.write('<style:graphic-properties style:run-through="foreground" style:wrap="none" style:horizontal-pos="center" style:horizontal-rel="paragraph" style:mirror="none" fo:clip="rect(0in, 0in, 0in, 0in)" draw:luminance="0%" draw:contrast="0%" draw:red="0%" draw:green="0%" draw:blue="0%" draw:gamma="100%" draw:color-inversion="false" draw:image-opacity="100%" draw:color-mode="standard"/>\n')
    contentXml.write('</style:style>\n')
    contentXml.write('</office:automatic-styles>\n')
    contentXml.write('<office:body>\n')
    contentXml.write('<office:text text:use-soft-page-breaks="true">\n')

    # Counting pages for current lmde file
    contentLmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
    contentDefaultStyleLen = len(contentLmdeFilesDefaultStyle.readlines())
    contentLmdeFilesDefaultStyle.close()

    if leftHeaderValidate == True and rightHeaderValidate == True:
        defaultStyleCount = 2
    else:
        defaultStyleCount = 0

    # Converting and copy the text from current lmde file
    while defaultStyleCount < contentDefaultStyleLen:
        if leftHeaderValidate == True and rightHeaderValidate == True:
            defaultStyleCountCheck = 2
        else:
            defaultStyleCountCheck = 0

        contentLmdeFilesDefaultStyle = open(directory+'/'+lmdeName+'.lmde', 'r')
        contentDefaultStyleAll = contentLmdeFilesDefaultStyle.readlines()[defaultStyleCount]
        contentDefaultStyleVar = contentDefaultStyleAll.split(' ')[0]

        if defaultStyleCount == defaultStyleCountCheck:
            tagVar = 'P1'
            lmdeTags_func(directory, contentDefaultStyleAll, contentDefaultStyleVar, contentXml, tagVar)

        else:
            if '#' == contentDefaultStyleVar:
                tagVar = 'h1'
            if '##' == contentDefaultStyleVar:
                tagVar = 'h2'
            if '###' == contentDefaultStyleVar:
                tagVar = 'h3'
            if '$' == contentDefaultStyleVar:
                tagVar = 'p1'
            if '$^' == contentDefaultStyleVar:
                tagVar = 'p1dc'
            if '$$' == contentDefaultStyleVar:
                tagVar = 'p2'
            if '[png]' in contentDefaultStyleVar:
                tagVar = 'i'
            if '[toc]' in contentDefaultStyleVar:
                tagVar = 'toch'
            lmdeTags_func(directory, contentDefaultStyleAll, contentDefaultStyleVar, contentXml, tagVar)

        defaultStyleCount += 1
    contentLmdeFilesDefaultStyle.close()

    contentXml.write('</office:text>\n')
    contentXml.write('</office:body>\n')
    contentXml.write('</office:document-content>')
    contentXml.close()