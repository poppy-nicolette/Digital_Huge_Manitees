#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 08:29:57 2022

@author: nicolapoppy
"""

import pandas as pd
import os

working_dir = '/Users/nicolapoppy/Desktop/CODING_WORKING/Python/LIBRARIES/OCR_text_analysis'
os.chdir(working_dir)
os.getcwd()

#to export
conda env export > OCR_with_pytesseract.yaml --from-history

# to import
conda env create -f OCR_with_pytesseract.yaml

# to activate
conda activate OCR_with_pytesseract

