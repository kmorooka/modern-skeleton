# --------------------------------------------------------
# File: skeleton.py
# Version: v1.0
# AsOf : 2022.6.15
# Fuction:
#   Skeleton sample code for learning. Upload file, do anything the uploaded file, zip the output directory, file download.
# --------------------------------------------------------
import sys
import os, time
import shutil
import re
import threading

ZIP_FNAME = 'skeleton' # zip for all files.
# 並列処理を可能にするため、出力先ファイルパスをスレッド毎に保存する。
output = threading.local()

# ----------------------------------------------------
# zip_files() 
#    arg: directory path to zip.
# ----------------------------------------------------
def zip_files(dirname):
    # print('--- zip_files() : Starting ...') 
    print('--- zip_files(): dirname= {}'.format(dirname))
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
    print('--- proc_file() : Starting ...') 
    # print('--- proc_file : fn = {}'.format(fn))
    # print('--- proc_file : out = {}'.format(out))

    # Write code to do something!
    # In this case, copy uploaded file to tmp dir & zip & download.
    fname = os.path.basename(fn)
    fout = out + '/' + fname
    # print('--- proc_file(): fout = {}'.format(fout))
    shutil.copyfile(fn, fout)

    return(0)
# ----------------------------------------------------
# main() 
#   fn: Uploaded full-path file name w/ tmp current directory.
#   out: Temporary directory name for output.
# ----------------------------------------------------
def main(fn, out):
    print('--- main() : Starting ...') 
    # print('--- main: fn = {}'.format(fn)) 
    output.path = out
    # print('--- main: output.path = {}'.format(output.path))

    # proc_file(fn, out)
    # zip_files(out)
    proc_file(fn, output.path)
    zip_files(output.path)

    return(0)
# ----------------------------------------------------
# End of File
# ----------------------------------------------------
