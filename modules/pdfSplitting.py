#!/bin/python3

from pypdf import PdfWriter, PdfReader

def pdfSplitting_func(directory, template):
  print('\033[33m'+'Splitting bilingual pdf file in half'+'\033[0m')
  pdfSplittingReader = PdfReader(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf')
  pdfSplittingLen = len(pdfSplittingReader.pages)

  pdfSplittingWriter = PdfWriter()

  pdfSplittingCount = 0
  while pdfSplittingCount < int(pdfSplittingLen):
      pdfSplittingReader.pages[pdfSplittingCount].mediabox.right = (pdfSplittingReader.pages[pdfSplittingCount].mediabox.right / 2)
      pdfSplittingWriter.add_page(pdfSplittingReader.pages[pdfSplittingCount])
      pdfSplittingLeft = open(directory+'/.mde2pdfTmp/pdf-c/'+template+'-left.pdf', 'wb')
      pdfSplittingWriter.write(pdfSplittingLeft)
      pdfSplittingLeft.close()
      pdfSplittingCount += 1
  pdfSplittingWriter.close()

  pdfSplittingReader = PdfReader(directory+'/.mde2pdfTmp/pdf-c/'+template+'.pdf')
  pdfSplittingLen = len(pdfSplittingReader.pages)

  pdfSplittingWriter = PdfWriter()

  pdfSplittingCount = 0
  while pdfSplittingCount < int(pdfSplittingLen):
      pdfSplittingReader.pages[pdfSplittingCount].mediabox.left = (pdfSplittingReader.pages[pdfSplittingCount].mediabox.right / 2)
      pdfSplittingWriter.add_page(pdfSplittingReader.pages[pdfSplittingCount])
      pdfSplittingRight = open(directory+'/.mde2pdfTmp/pdf-c/'+template+'-right.pdf', 'wb')
      pdfSplittingWriter.write(pdfSplittingRight)
      pdfSplittingRight.close()
      pdfSplittingCount += 1
  pdfSplittingWriter.close()

  pdfSplittingLeft = open(directory+'/.mde2pdfTmp/pdf-c/'+template+'-left.pdf', 'rb')
  pdfSplittingRight = open(directory+'/.mde2pdfTmp/pdf-c/'+template+'-right.pdf', 'rb')

  pdfSplittingWriter = PdfWriter()

  pdfSplittingLeftCount = 0
  pdfSplittingRightCount = 1
  while pdfSplittingLeftCount < int(pdfSplittingLen):
    pdfSplittingWriter.append(fileobj=pdfSplittingLeft, pages=(pdfSplittingLeftCount, pdfSplittingRightCount))
    pdfSplittingWriter.append(fileobj=pdfSplittingRight, pages=(pdfSplittingLeftCount, pdfSplittingRightCount))
    pdfSplittingLeftCount += 1
    pdfSplittingRightCount += 1

  pdfSplittingMerged = open(directory+'/.mde2pdfTmp/pdf-c/'+template+'-half.pdf', 'wb')
  pdfSplittingWriter.write(pdfSplittingMerged)
  pdfSplittingMerged.close()
  pdfSplittingWriter.close()