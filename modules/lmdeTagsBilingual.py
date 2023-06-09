#!/bin/python3

from PIL import Image

def lmdeTagsBilingual_func(directory, contentDefaultStyleAll, contentDefaultStyleVar, contentXml, tagVar, defaultStyleCount):
    # Creating h1 tag
    if '#' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('# ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating h2 tag
    if '##' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('## ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating h3 tag
    if '###' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('### ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating p1 tag
    if '$' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('$ ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating p1dc tag
    if '$^' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('$^ ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating p2 tag
    if '$$' == contentDefaultStyleVar:
        contentTag = ''
        contentTag = contentDefaultStyleAll.replace('$$ ', '<text:p text:style-name="'+str(tagVar)+'">\n', 1)
        boldCount = 1
        boldCountLen = contentDefaultStyleAll.count('**') + 1
        while boldCount < boldCountLen:
            if (boldCount % 2) == 0:
                contentTag = contentTag.replace('**', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('**', '<text:span text:style-name="tb">', 1)
            boldCount += 1
        italicCount = 1
        italicCountLen = contentDefaultStyleAll.count('__') + 1
        while italicCount < italicCountLen:
            if (italicCount % 2) == 0:
                contentTag = contentTag.replace('__', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('__', '<text:span text:style-name="ti">', 1)
            italicCount += 1
        redCount = 1
        redCountLen = contentDefaultStyleAll.count('``') + 1
        while redCount < redCountLen:
            if (redCount % 2) == 0:
                contentTag = contentTag.replace('``', '</text:span>', 1)
            else:
                contentTag = contentTag.replace('``', '<text:span text:style-name="tr">', 1)
            redCount += 1
        footnoteCount = 1
        footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
        while footnoteCount < footnoteCountLen:
            if '[^]' in contentTag:
                contentTag = contentTag.replace('[^][(', '<text:note text:note-class="footnote"><text:note-citation></text:note-citation><text:note-body><text:p text:style-name="fn">', 1)
                contentTag = contentTag.replace(')]', '</text:p></text:note-body></text:note>', 1)
            footnoteCount += 1
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write(contentTag+'</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating png tag
    if '[png]' in contentDefaultStyleVar:
        imgLocation = directory+'/'+contentDefaultStyleVar.split('(')[1].split(')')[0]
        img = Image.open(imgLocation)
        getDPI = str(img.info).split('(')[1]
        xDPI = str(getDPI).split(',')[0]
        yDPI = str(getDPI).split(' ')[1].split(')')[0]
        widthInches = img.width / float(xDPI)
        heightInches = img.height / float(yDPI)
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write('<text:p text:style-name="'+str(tagVar)+'">\n')
            contentXml.write('<draw:frame draw:style-name="fr1" draw:name="Image1" text:anchor-type="char" svg:width="'+str(widthInches)+'in" svg:height="'+str(heightInches)+'in" draw:z-index="0">\n')
            contentXml.write('<draw:image xlink:href="'+str(imgLocation)+'" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:filter-name="&lt;All images&gt;" draw:mime-type="image/png"/>\n')
            contentXml.write('</draw:frame>\n')
            contentXml.write('</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write('<text:p text:style-name="'+str(tagVar)+'">\n')
            contentXml.write('<draw:frame draw:style-name="fr1" draw:name="Image1" text:anchor-type="char" svg:width="'+str(widthInches)+'in" svg:height="'+str(heightInches)+'in" draw:z-index="0">\n')
            contentXml.write('<draw:image xlink:href="'+str(imgLocation)+'" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:filter-name="&lt;All images&gt;" draw:mime-type="image/png"/>\n')
            contentXml.write('</draw:frame>\n')
            contentXml.write('</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')

    # Creating toc tag
    if '[toc]' in contentDefaultStyleVar:
        contentTag = ''
        tocCheck = False
        tocHeader = contentDefaultStyleAll.replace('[toc](', '').replace(')', '')
        if (defaultStyleCount % 2) == 0:
            contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write('<text:p text:style-name="'+str(tagVar)+'">\n')
            contentXml.write(tocHeader)
            contentXml.write('</text:p>\n')
            contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
        else:
            contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
            contentXml.write('<text:p text:style-name="'+str(tagVar)+'">\n')
            contentXml.write(tocHeader)
            contentXml.write('</text:p>\n')
            contentXml.write('</table:table-cell></table:table-row>\n')
            tocCheck = True

        pageNumberFileOpen = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'r')
        pageNumberFileLen = len(pageNumberFileOpen.readlines())
        pageNumberFileOpen.close()

        if tocCheck == True:
            pageNumberFileCount = 0
            while pageNumberFileCount < pageNumberFileLen:
                pageNumberFileOpen = open(directory+'/.mde2pdfTmp/pn/pageNumberFile.txt', 'r')
                contentDefaultStyleAll = pageNumberFileOpen.readlines()[pageNumberFileCount]
                contentTag = contentDefaultStyleAll.replace('## ', '<text:p text:style-name="toc">\n', 1)
                boldCount = 1
                boldCountLen = contentDefaultStyleAll.count('**') + 1
                while boldCount < boldCountLen:
                    contentTag = contentTag.replace('**', '', 1)
                    boldCount += 1
                italicCount = 1
                italicCountLen = contentDefaultStyleAll.count('__') + 1
                while italicCount < italicCountLen:
                    contentTag = contentTag.replace('__', '', 1)
                    italicCount += 1
                redCount = 1
                redCountLen = contentDefaultStyleAll.count('``') + 1
                while redCount < redCountLen:
                    contentTag = contentTag.replace('``', '', 1)
                    redCount += 1
                footnoteCount = 1
                footnoteCountLen = contentDefaultStyleAll.count('[^]') + 1
                while footnoteCount < footnoteCountLen:
                    if '[^]' in contentTag:
                        firstDelPos=contentTag.find('[^][(', 1)
                        secondDelPos=contentTag.find(')]', 1)
                        contentTag = contentTag.replace(contentTag[firstDelPos:secondDelPos+2], '')
                    footnoteCount += 1
                contentTag = contentTag.replace('[(#', '<text:tab/>', 1)
                contentTag = contentTag.replace('#)]', '\n</text:p>', 1)
                if (pageNumberFileCount % 2) == 0:
                    contentXml.write('<table:table-row table:style-name="Table1.1"><table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
                    contentXml.write(contentTag)
                    contentXml.write('</table:table-cell><table:table-cell table:style-name="Table1.A1" office:value-type="string"><text:p text:style-name="'+str(tagVar)+'"></text:p></table:table-cell>\n')
                else:
                    contentXml.write('<table:table-cell table:style-name="Table1.A1" office:value-type="string">\n')
                    contentXml.write(contentTag)
                    contentXml.write('</table:table-cell></table:table-row>\n')
                pageNumberFileOpen.close()
                pageNumberFileCount += 1