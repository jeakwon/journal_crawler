#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import docx

document = docx.Document()

f = open('20180119_Nat_Neuro.csv', 'r', encoding='utf-8')
rows = csv.reader(f)
for row in rows:
    print(row)
    p = document.add_paragraph(row)
    # for row in rows:
        # print(' '.join(row))
f.close()

document.save('20180119_Nat_Neuro.docx')
