# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 31, 2018
# Modifi: Sep 21, 2018

import re
import ntpath

from siki.basics.Exceptions import NoAvailableResourcesFoundException

def gen_folderpath(strPrev, *strLast):
    import os
    strDir = strPrev
    for strL in strLast:
        strDir = os.path.join(strDir, strL)
    return strDir


def gen_filepath(strFolder, strFilename, strSuffix=None, strAddition=None):
    import os
    strDir = os.path.join(strFolder, gen_filename(strFilename, strSuffix, strAddition))
    return os.path.abspath(strDir)


def gen_filename(strFilename, strSuffix=None, strAddition=None):
    if strSuffix is None and strAddition is not None:
        return strFilename + "." + strAddition
    if strSuffix is None and strAddition is None:
        return strFilename
    if strSuffix is not None and strAddition is None:
        return strFilename + "." + strSuffix
    
    return strFilename + "." + strAddition + "." + strSuffix


def read_file(strFilepath, nReadSize = 4096, callback_func=None):
    with open(file=strFilepath, mode="rb") as f:

        if not f.readable(): 
            raise NoAvailableResourcesFoundException("Cannot load file")
        
        if callback_func is not None:
            data = f.read(nReadSize)
            while data is not None and len(data) > 0:
                callback_func(data)
                data = f.read(nReadSize)
        else:
            return f.read()



def write_file(strFilepath, rawData, bAppend=False):
    if not bAppend:
        f = open(file=strFilepath, mode="wb")
    else:
        f = open(file=strFilepath, mode="a+b")

    if not f.writable():
        raise NoAvailableResourcesFoundException("Cannot write file")

    if rawData is not None and len(rawData) > 0:
        f.write(rawData)


def touch_file(strFilepath):
    f = open(strFilepath, "w")
    f.close()


def mkdir(strDirectory):
    import os
    if not os.path.exists(strDirectory):
        os.makedirs(strDirectory)


def rmfile(strFilepath):
    import os
    if not os.path.exists(strFilepath):
        raise NoAvailableResourcesFoundException("File path is not existed!")
    os.remove(strFilepath)


def rmdir(strFolder):
    import os
    if not os.path.exists(strFolder):
        raise NoAvailableResourcesFoundException("Directory path is not existed!")
    os.rmdir(strFolder)


def search_files(strFolderPath, pattern="*"):

    lFiles = _file_ite(strFolderPath)
    return _file_filtering(lFiles, pattern)


def search_folders(strFolderPath):
    import os
    lDirs = []
    for i in os.listdir(strFolderPath):
        path = os.path.join(strFolderPath, i)
        if os.path.isdir(path):
            lDirs.extend(search_folders(path))
        lDirs.append(path)
    return lDirs


def root_leaf(path):
    """
    return root, leaf
    """
    head, tail = ntpath.split(path)
    return ntpath.basename(head), tail


def _file_ite(strFolderPath):
    import os

    flist = []
    for i in os.listdir(strFolderPath):
        path = os.path.join(strFolderPath, i)
        if os.path.isdir(path):
            flist.extend(_file_ite(path))
        else:
            flist.append(path)
    return flist
    

def _file_filtering(lfs, pattern):
    l = []
    if "*" == pattern:
        l.extend(lfs)
    else:
        for f in lfs:
            if re.search(pattern, f):
                l.append(f)
    return l