# -*- coding: utf-8 -*-
# -----------------------------
from os import chdir, getcwd
import PyPDF2

chdir("E:/Project/Python_Projects/Test_Data/PDFs")

with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
# -----------------------------
