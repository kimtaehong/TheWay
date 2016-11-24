#-*- coding: utf-8 -*-
import os
import sqlite3
import exifread
import time
import datetime
import hashlib
import collections
import re
import xlrd
import urllib
import sys
import pdb

#############################################################
######################## convert ############################
#############################################################

def tag2timestamp(s) :
    return int(time.mktime(time.strptime(s.printable, "%Y:%m:%d %H:%M:%S"))) #2016:05:18 00:29:51

def rePath() :
    return os.getcwd().replace('\\', '/')

def toString(value):
   return str(value)

def deleteResult() :
    os.system("del result.db")

def md5(file) :
    return hashlib.md5(file).hexdigest()

def sha1(file) :
    return hashlib.sha1(file).hexdigest()

def retTags(f) :
    return exifread.process_file(f)

#############################################################
#############################################################
#############################################################

tableDic = ['appName',
            'packageName',
            'path',
            'tableName',
            'time',
            'position',
            'positionX',
            'positionY',
            'start',
            'startX',
            'startY',
            'end',
            'endX',
            'endY',
            'search',
            'searchX',
            'searchY',
            'Seperate',
            'DataType']

def list2dic(record) :
    ret = collections.OrderedDict()
    for i in range(0, len(tableDic)) :
        if record[i] != u'' :
            ret[tableDic[i]] = record[i]
    return ret

#############################################################
#############################################################
#############################################################

def xmlOpen(packageName, path) :
    return open('./phone/data/' + packageName + '/' + path, 'rb').read()

def findAll(data, regex) :
    for reg in regex.split('&&&&') :
        if type(data) == list :
            data = data[0]
        data = re.findall(reg, data)
    return data

def append(inValue, data) :
    return inValue.append(data)

#############################################################
#############################################################
#############################################################

def connectXls(file) :
    File = xlrd.open_workbook(file)
    sheetNames = File.sheet_names()[0]
    sheet = File.sheet_by_name(sheetNames)
    return sheet

def xlsSize(file) :
    sheet = connectXls(file)
    row = sheet.nrows
    col = sheet.ncols
    return row, col

def locToCoord(location) :
    url = "http://maps.googleapis.com/maps/api/geocode/xml?address=" + urllib.parse.quote(location) + "&language=ko&sensor=false"
    data = urllib.request.urlopen(url).read()
    if type(data) == str() :
        locations = data.replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')
    elif type(data) == bytes():
        locations = data.decode('utf-8').replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')
    elif True :
        locations = data.decode('utf-8').replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')
    location = re.findall('<location>(.+?)</location>', locations)[0]
    lat = re.findall('<lat>(.+?)</lat>', location)[0]
    lon = re.findall('<lng>(.+?)</lng>', location)[0]
    return lat, lon

def timeTotimestamp(timeS) :
    try:
        return int(time.mktime(time.strptime(timeS, "%Y-%m-%d %H:%M:%S")))
    except :
        print(timeS)
#############################################################
#############################################################
#############################################################