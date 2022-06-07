"""
#!/Users/morookak/opt/anaconda3/bin/python
# coding:utf-8
"""
"""
#!/usr/bin/python 
File: apa_auto.py
Fuction: Skeleton sample code for Container, SaaS.
Version: v1.0
"""
import sys
import os, time
import shutil
# from shutil import make_archive
import re
# from matplotlib.colors import Normalize
# import pandas as pd
# import matplotlib as mpl
mpl.use("Agg")  # To avoid Assertion ~~ error in flask & matplotlib.
# import matplotlib.pyplot as plt
# import seaborn as sns
from apa_config import *  # Read Excel column name from apa-config.py file.
import threading


# 並列処理を可能にするため、出力先ファイルパスをスレッド毎に保存する。
output = threading.local()

# ----------------------------------------------------
# zip_files() 
#    arg: directory path to zip for plot files.
# ----------------------------------------------------
def zip_files(dirname):

    print('zip_files(): dirname= {}'.format(dirname))
    shutil.make_archive(ZIP_FNAME, 'zip', root_dir=dirname)
    shutil.move(ZIP_FNAME + '.zip', dirname)
    return(0)

# ----------------------------------------------------
# proc_file() 
# ----------------------------------------------------
def proc_file(fn):
    
    print('proc_file() : file name = {}'.format(fn))
    return(0)
# ----------------------------------------------------
# main_plot() 
#    arg: Uploaded & stored Excel full-path file name.
# ----------------------------------------------------
def main_plot(fn, out):
    print('modern-skeleton : Starting ...') 
    print('modern-skeleton: Excel file = {}'.format(fn)) 

    output.path = out
    proc_file(fn)    # process input file.

    zip_files(out)
    print('modern-skeleton : Program End.')

    return(0)
# ----------------------------------------------------
# End of File
# ----------------------------------------------------
