# --------------------------------------------------------
# File: skeleton.py
# Version: v1.0
# AsOf : 2022.6.8
# Fuction:
#     Skeleton sample code for learning. Upload file, do anything the uploaded file, zip the output directory, file download.
# --------------------------------------------------------
import sys
import os, time
import shutil
import re
import threading

ZIP_FNAME = 'modern-skeleton' # zip for all plot png files.

# 並列処理を可能にするため、出力先ファイルパスをスレッド毎に保存する。
output = threading.local()

# ----------------------------------------------------
# zip_files() 
#    arg: directory path to zip for files.
# ----------------------------------------------------
def zip_files(dirname):
    print('--- zip_files: dirname= {}'.format(dirname))
    shutil.make_archive(ZIP_FNAME, 'zip', root_dir=dirname)
    shutil.move(ZIP_FNAME + '.zip', dirname)
    return(0)

# ----------------------------------------------------
# proc_file() 
#   fn: 相対パス名
#   out: 出力ディレクトリパス名
#   fnからファイル名部分だけ抜き出し、outディレクトリ名とつないでコピー
#   なにか処理したい場合、ここにコードを書く
# ----------------------------------------------------
def proc_file(fn, out):
    fname = os.path.basename(fn)  
    fout = out + '/' + fname
    print('--- proc_file: fout = {}'.format(fout)) 
    shutil.copyfile(fn, fout)  # do nothing, copy file only.
    return(0)

# ----------------------------------------------------
# main_plot() 
#   fn: Uploaded full-path file name w/ tmp current directory.
#   out: Temporary directory name for output.
# ----------------------------------------------------
def main(fn, out):
    print('--- main: Starting ...') 
    print('--- main: fn = {}'.format(fn)) 
    print('--- main: out = {}'.format(out)) 

    proc_file(fn, out)    # process input file.
    zip_files(out)   # zip directory.

    print('--- main: Program End.')

    return(0)
# ----------------------------------------------------
# End of File
# ----------------------------------------------------
