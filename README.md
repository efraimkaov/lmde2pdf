# lmde2pdf

### This application generates pdf files from lmde plain text files based on templates for Liturgical Services Books

![lmde2pdf](https://github.com/efraimkaov/lmde2pdf/assets/63643635/ba6e30d1-4ff6-4380-8a49-82aaf0bdc85e)

### What are lmde files

* **lmde** stands for **Like Mark Down Extended**

* **lmde** is a plain text file with **.lmde** extension and markdown inspired syntax

## lmde syntax

```
# Heading1
## Heading2
### Heading3
$ Paragraph1
$^ Paragraph1 with drop caps
$$ Paragraph2

[png](link.png)

**Bold text**
__Italicized text__
``Red text``

[^][(Footnote)]

[lh](Left header text)
[rh](Right header text)
```

### Dependencies

* Python3 >= 3.9.2

* LibreOffice Writer >= 7.0.4.2

## Installation (in progress)

```sh
git clone https://github.com/efraimkaov/lmde2pdf.git
cd lmde2pdf/
pip3 install -r requirements.txt
```
## How to use (in progress)

```sh
# for gui
python3 lmde2pdf.py
# for cli
python3 lmde2pdf-cli.py
```

### lmde2pdf-cli.py examples

```sh
# for regular books
python3 lmde2pdf-cli.py -t stdrb -l1 el-GR -d /opt/lmde2pdf/examples/regular
```

```sh
# for bilingual books
python3 lmde2pdf-cli.py -t blgrb -l1 ro-RO -l2 el-GR -d /opt/lmde2pdf/examples/regular-bilingual
```

### Features

* template for regular books

* template for bilingual books

* borders

* left and right headers

* page numbering

* foot notes

* drop caps

* bold and italic text

* template with default text bold (on this template bold syntax will make the text normal)

* hyphenation

* images

* table of content

### To-Do List

* **GUI** for **lmde2pdf** - in progress

* more templates

* documentation for installation in Linux, macOS and Windows

* documentation how to create templates

#### If you find a bug please open a new issue and send a Bug report.

##### If someone test this application in macOS or Windows please let me know if works or not (only tested in Linux)!
