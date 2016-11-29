import util
import dbutil
import appParse
from twpoint.models import Application, WayPoint, BaseStation, Picture
import pdb


def sqlParse(record, path):
    query, values = dbutil.genQuery(record)
    appcon = dbutil.appdbconnect(record['packageName'], record['path'], path)
    appcursor = appcon.cursor()
    appcursor.execute(query)
    while True:
        appRecord = appcursor.fetchone()
        if appRecord is None:
            break
        pdb.set_trace()
        insertQuery = dbutil.appQuery(record, appRecord, values)
        dbutil.inputResDB(insertQuery)


def xmlParse(record, path):
    record['tableName'] = ''
    xmlcon = util.xmlOpen(record['packageName'], record['path'], path)
    if 'Sperate' in record:
        appRecords = xmlcon.split(record['Seperate'])
    else:
        appRecords = [xmlcon]
    valueList = []
    for key in record.keys()[3:-2] : #First 3 == appName, packageName, path End 2 == Sperate, dataType
        if key == 'Sperate':
            pass
        if record[key] != '':
            valueList.append(key)

    for appRecord in appRecords:
        datas = []
        for re in record.keys()[3:-2]:
            reData = util.findAll(appRecord, record[re])[0]
            datas.append(reData)
        insertQuery = dbutil.appQuery(record, datas, valueList)
        dbutil.inputResDB(insertQuery)


def fileParse(record):
    return appParse.parse(record['appName'], record['packageName'], record['path'], record['tableName'])


def appdata(target):
    con = dbutil.appdata()
    cursor = con.cursor()
    cursor.execute("select * from appinfo;")
    while True:
        record = cursor.fetchone()
        if record is None:
            break
        record = util.list2dic(record)
        if record['DataType'] == 'SQL':
            sqlParse(record, target)
        elif record['DataType'] == 'XML':
            xmlParse(record, target)
        elif record['DataType'] == 'File':
            fileParse(record)
        else:
            return False
