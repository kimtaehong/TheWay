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
import urllib.request

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
            'point_time',
            'position',
            'position_x',
            'position_y',
            'start',
            'start_x',
            'start_y',
            'end',
            'end_x',
            'end_y',
            'search',
            'search_x',
            'search_y',
            'Seperate',
            'DataType']


def list2dic(record):
    ret = collections.OrderedDict()
    for i in range(0, len(tableDic)):
        if record[i] != u'':
            ret[tableDic[i]] = record[i]
    return ret

#############################################################
#############################################################
#############################################################

def xmlOpen(packageName, path, folderpath) :
    return open(folderpath + '/data/' + packageName + '/' + path, 'rb').read()

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

    try :
        tmp_location = re.findall('<location>(.+?)</location>', locations)[0]
        lat = re.findall('<lat>(.+?)</lat>', tmp_location)[0]
        lon = re.findall('<lng>(.+?)</lng>', tmp_location)[0]
    except :
        if location.count('-') == 0 :
            return False, False
        else :
            return locToCoord(location.split('-')[0])
    return lat, lon


def timeTotimestamp(timeS):
    try:
        return int(time.mktime(time.strptime(timeS, "%Y-%m-%d %H:%M:%S")))
    except :
        print(timeS)

#############################################################
#############################################################
#############################################################
def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    return dd

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    before_dd = dms2dd(parts[0], parts[1], parts[2], parts[3])
    return before_dd

def toLoc(x, y) :
    url  = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(y) + ',' + str(x) + '&language=ko'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    try :
        location  = re.findall('"formatted_address" : "(.+?)"', html)[0]
    except :
        return False
    return location

def cutting(loc) :
    levels = loc.split(' ')
    if re.match('[0-9, -]+', levels[-1]) :
        return levels[1:-1]
    else :
        return levels[1:]

def isNotNone(a, b) :
    if a != None and b != None :
        return True
    else :
        return False
