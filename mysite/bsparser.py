#-*- coding: utf-8 -*-
import util
import dbutil


def CSVcolunmMatch(row):
    Data = {}
    Matcher = {
        'time': ['시화시각', '통화시작시간'],
        'day': ['시화일자'],
        'position': ['발신기지국주소', '발신SITE'],
        'sender': ['발신번호'],
        'receiver': ['요청전화번호', '착신번호'],
        'type': ['사용유형', '구분']
    }
    row = row.split(',')
    for i in range(0, len(row)):
        for dataTypes in Matcher.keys():
            for dataType in Matcher[dataTypes]:
                if dataType == row[i] :
                    Data[dataTypes] = i
    return Data


def XLScolunmMatch(row):
    Data = {}
    Matcher = {
        'time': [u'시화시각', u'통화시작시간'],
        'day': [u'시화일자'],
        'position': [u'발신기지국주소', u'발신SITE'],
        'sender': [u'발신번호'],
        'receiver': [u'요청전화번호', u'착신번호'],
        'type': [u'사용유형', u'구분']
    }
    for i in range(0, len(row)):
        for dataTypes in Matcher.keys():
            for dataType in Matcher[dataTypes]:
                if dataType == row[i]:
                    Data[dataTypes] = i
    return Data


def findRow_csv(data):
    lenTmp = 0
    position = 0
    for row in data:
        row = row.split(',')
        if lenTmp == len(row) and lenTmp > 3:
            return position - 1
        lenTmp = len(row)
        position += 1


def findRow_xls(xls):
    idx = 0
    cols = xls.ncols
    while True:
        if xls.row_values(idx)[cols-1] != u'':
            return idx
        idx += 1


def csvParse(file):
    csv = file.split('\r\n')
    idx = findRow_csv(csv)
    Matchers = CSVcolunmMatch(csv[idx])

    l = len(csv) - idx
    i = 0

    for row in csv[idx+1:]:
        i += 1
        row = row.split(',')
        rowData = {}
        for Matcher in Matchers.keys():
            if row == ['']:
                continue
            rowData[Matcher] = row[int(Matchers[Matcher])]
        dbutil.bsQuery(rowData)


def xlsParse(file):
    xls = util.connectXls(file)
    idx = findRow_xls(xls)
    Matchers = XLScolunmMatch(xls.row_values(idx))
    length = xls.nrows

    l = length - idx
    i = 0

    for line in range(idx+1, length) :
        i += 1
        row = xls.row_values(line)
        rowData = {}
        for Matcher in Matchers.keys() :
            if row == [''] :
                continue
            rowData[Matcher] = row[int(Matchers[Matcher])]
        dbutil.bsQuery(rowData)


def parse(filename, file):
    if filename.split('.')[-1].lower() == 'csv':
        csvParse(file)
    elif file.split('.')[-1].lower() == 'xls':
        xlsParse(file)