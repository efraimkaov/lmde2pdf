#!/bin/python3

def manifestXml_func(directory):
    print('\033[33m'+'Generating manifest.xml'+'\033[0m')
    manifestXml = open(directory+'/.mde2pdfTmp/odt-u/META-INF/manifest.xml', 'a')
    manifestXml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    manifestXml.write('<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.3" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0">\n')
    manifestXml.write(' <manifest:file-entry manifest:full-path="/" manifest:version="1.3" manifest:media-type="application/vnd.oasis.opendocument.text"/>\n')
    manifestXml.write(' <manifest:file-entry manifest:full-path="manifest.rdf" manifest:media-type="application/rdf+xml"/>\n')
    manifestXml.write(' <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>\n')
    manifestXml.write(' <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>\n')
    manifestXml.write('</manifest:manifest>')
    manifestXml.close()