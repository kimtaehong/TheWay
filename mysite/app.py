import util
import dbutil
import appParse
from twpoint.models import Application, WayPoint
import pdb
import after


def sqlParse(record, path, afterprocess):
    query, values = dbutil.genQuery(record)
    try:
        appcon = dbutil.appdbconnect(record['packageName'], record['path'], path)
        appcursor = appcon.cursor()
        appcursor.execute(query)  # get data
    except:
        return False  # Except None file

    if len(Application.objects.filter(app_name=record['appName'])) == 0:
        ap = Application(app_name = record['appName'], app_package = record['packageName'])
        ap.save()
    else :
        ap = Application.objects.filter(app_name = record['appName'])[0]

    while True:
        appRecord = appcursor.fetchone()
        if appRecord is None:
            break
        rec = WayPoint(app_name_id = ap.id, path = record['path'], table_name = record['tableName'])
        for i in range(0, len(values)):
            rec.__dict__[values[i]] = appRecord[i]
        rec.save()
    if afterprocess != '':
        after.process(afterprocess)


def xmlParse(record, path, afterprocess):
    try:
        record['tableName'] = ''
        xmlcon = util.xmlOpen(record['packageName'], record['path'], path)
    except:
        return False

    if len(Application.objects.filter(app_name=record['appName'])) == 0:
        ap = Application(app_name = record['appName'], app_package = record['packageName'])
        ap.save()
    else :
        ap = Application.objects.filter(app_name = record['appName'])[0]

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
        rec = WayPoint(app_name_id = ap.id, path = record['path'], table_name = record['tableName'])
        for i in range(0, len(values)) :
            rec.__dict__[values[i]] = appRecord[i]
        rec.save()
        if afterprocess != '' :
            after.process(afterprocess)

def fileParse(record, target):
    return appParse.Parse(record['appName'],
                          record['packageName'],
                          record['path'],
                          record['tableName'],
                          target)

def appdata(target) :
    con = dbutil.appdata()
    cursor = con.cursor()
    cursor.execute("select * from appinfo;")
    while True:
        record = cursor.fetchone()
        if record is None:
            break
        record = util.list2dic(record)
        print (record)
        if record['DataType'].split('_')[0] == 'SQL':
            sqlParse(record, target, record['DataType'].split('_')[1])
        elif record['DataType'].split('_')[0] == 'XML':
            xmlParse(record, target, record['DataType'].split('_')[1])
        elif record['DataType'] == 'File':
            fileParse(record, target)
        else:
            return False
