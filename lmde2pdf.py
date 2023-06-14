#!/bin/python3

import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from modules.lmde2pdfMain import lmde2pdf_func
from ttkthemes import ThemedTk

guiCheck = True

directory = ''
def directory_func():
    global directory
    directory = askdirectory(title='Select the full path for the input directory')

installationDir = os.path.dirname(__file__)

with open(installationDir+'/templates/languages-code.txt') as inFile:
    languageLines = [line for line in inFile]
    languageTuple = tuple(sub.replace('\n', '') for sub in languageLines)

with open(installationDir+'/templates/template.cfg') as inFile:
    templateLines = [line for line in inFile]
    templateTuple = tuple(sub.replace('\n', '') for sub in templateLines)

template_image = ''

def template_func(event):
    global template_image

    templateName = event.widget.get().split('-')[1]

    templateImage = installationDir+'/templates/'+templateName+'/template.png'

    template_image = tk.PhotoImage(file=templateImage)
    templateImage_label = ttk.Label(main_frame, image=template_image)
    templateImage_label.grid(row=0, column=4, rowspan=5, sticky='nsew')

def convert_func():
    if templateCurrent.get() == '':
        template = ''
        templateType = ''
    else:
        template = template_combobox.get().split('-')[1]
        templateType = template_combobox.get()
    if language1Current.get() == '':
        lang1 = ''
        ctry1 = ''
    else:
        lang1 = language1_combobox.get().split('-')[0]
        ctry1 = language1_combobox.get().split('-')[1]
    if language2Current.get() == '':
        lang2 = ''
        ctry2 = ''
    else:
        lang2 = language2_combobox.get().split('-')[0]
        ctry2 = language2_combobox.get().split('-')[1]

    lmde2pdf_func(guiCheck, installationDir, template, templateType, lang1, ctry1, lang2, ctry2, directory)

root = ThemedTk(theme='yaru')

root.geometry('800x280')
root.minsize(800, 280)
root.maxsize(800, 280)
root.title('lmde2pdf.py')

main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5,anchor='center')

template_label = ttk.Label(main_frame, text='Template', font=('Arial', 17))
template_label.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=(0, 10), pady=(0, 10))

templateCurrent = tk.StringVar()
template_combobox = ttk.Combobox(main_frame, state='readonly', textvariable=templateCurrent, values=templateTuple)
template_combobox.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=(0, 10), pady=(0, 10))
template_combobox.bind('<<ComboboxSelected>>', template_func)

language1_label = ttk.Label(main_frame, text='Language1', font=('Arial', 17))
language1_label.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=(0, 10), pady=(0, 10))

language1Current = tk.StringVar()
language1_combobox = ttk.Combobox(main_frame, state='readonly', textvariable=language1Current, values=languageTuple)
language1_combobox.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=(0, 10), pady=(0, 10))

language2_label = ttk.Label(main_frame, text='Language2', font=('Arial', 17))
language2_label.grid(row=2, column=2, columnspan=2, sticky='nsew', padx=(0, 10), pady=(0, 10))

language2Current = tk.StringVar()
language2_combobox = ttk.Combobox(main_frame, state='readonly', textvariable=language2Current, values=languageTuple)
language2_combobox.grid(row=3, column=2, columnspan=2, sticky='nsew', padx=(0, 10), pady=(0, 10))

open_image = tk.PhotoImage(file='gui/folder-open.png')
open_btn = ttk.Button(main_frame, image=open_image, command=directory_func)
open_btn.grid(row=4, column=0, sticky='nsew', padx=(0, 10))

convert_btn = ttk.Button(main_frame, text='Convert', command=convert_func)
convert_btn.grid(row=4, column=1, columnspan=3, sticky='nsew', padx=(0, 10))

templateImage_label = ttk.Label(main_frame, font=('Arial', 17), width=23)
templateImage_label.grid(row=0, column=4, rowspan=5, sticky='nsew')

root.mainloop()