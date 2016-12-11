import dbutil
from twpoint.models import Application, WayPoint
import pdb
import util

def Parse(appName, packageName, path, tableName, target):
    if appName == 'appA' and path == 'fileA' :
        return appA_fileA(appName, packageName, path)
    elif appName == 'Cymera' and path == 'databases/cymeraGallery.db' :
        return cymera_cymeraGallery(appName, packageName, path, target)
    elif appName == 'GGulGGulMoneyBook' and path == 'databases/spending.db' :
        return GGulGGulMoneyBook_spending(appName, packageName, path, target)
    elif appName == 'KakaoTaxi' and path == 'databases/data.db' :
        return KakaoTaxi_data(appName, packageName, path, target)
    elif appName == 'Syrup' and path == 'databases/.C3PO_SensorDB.db' :
        return Syrup_sensor(appName, packageName, path, target)
    elif appName == 'BaedalTong' and path == 'databases/appboy.db' :
        return Beadaltong_ab(appName, packageName, path, target)


def appA_fileA(appName, packageName, path):
    #blank format
    #Analysis Code
    pass

def cymera_cymeraGallery(appName, packageName, path, target) :
    #Get Max value
    try :
        con    = dbutil.appdbconnect(packageName, path, target)
        cursor = con.cursor()
        cursor.execute("select photo_idx from cymera_photos order by photo_idx desc limit 0,1")
        Max = cursor.fetchone()[0]
    except :
        return

    ap = Application(app_name = appName, app_package = packageName)
    ap.save()

    for i in range(0, Max + 1) :
        cursor.execute("select photo_date from cymera_photos where photo_idx = " + str(i))
        data = cursor.fetchone()
        if type(data) == type(None) : #Notfound
            continue
        date = data[0]
        cursor.execute("select exif_latitude, exif_longitude from cymera_exif where photo_idx = '" + str(i) + "'")
        data = cursor.fetchone()
        if type(data) == type(None) : #Notfound
            continue
        lng = util.parse_dms(data[0])
        lat = util.parse_dms(data[1])

        input_data = WayPoint(path        = path,
                              table_name  = 'cymera_photos, cymera_exif',
                              position_x  = lng,
                              position_y  = lat,
                              point_time  = date,
                              app_name_id = ap.id)
        input_data.save()

def GGulGGulMoneyBook_spending(appName, packageName, path, target) :
    try :
        con    = dbutil.appdbconnect(packageName, path, target)
        cursor = con.cursor()
    except :
        return

    ap = Application(app_name = appName, app_package = packageName)
    ap.save()

    cursor.execute("select s_date, s_time, s_where from spendinglist")
    while True :
        data = cursor.fetchone()
        if data == None :
            break
        date = data[0] + " " + data[1]
        position = data[2]
        input_data = WayPoint(position = position,
                              point_time = date,
                              app_name_id = ap.id)
        input_data.save()

def KakaoTaxi_data(appName, packageName, path, target) :
    try :
        con    = dbutil.appdbconnect(packageName, path, target)
        cursor = con.cursor()
    except :
        return

    ap = Application(app_name = appName, app_package = packageName)
    ap.save()

    cursor.execute("select source, type, selected_at, v from location_item")
    while True :
        data = cursor.fetchone()
        if data == None :
            break
        if data[0] == 'HISTORY_START' :
            input_data = WayPoint(start = util.findAll(data[3], "\"name\":\"(.+?)\"")[0])
            input_data.start_x = util.findAll(data[3], "\"lng\":[0-9.]+")[0].split(":")[1]
            input_data.start_y = util.findAll(data[3], "\"lat\":[0-9.]+")[0].split(":")[1]
        elif data[0] == 'HISTORY_END' :
            input_data = WayPoint(end = util.findAll(data[3], "\"name\":\"(.+?)\"")[0])
            input_data.end_x = util.findAll(data[3], "\"lng\":[0-9.]+")[0].split(":")[1]
            input_data.end_y = util.findAll(data[3], "\"lat\":[0-9.]+")[0].split(":")[1]
        input_data.point_time = data[2]
        input_data.app_name_id = ap.id
        input_data.save()

def Syrup_sensor(appName, packageName, path, target) :
    try :
        con    = dbutil.appdbconnect(packageName, path, target)
        cursor = con.cursor()
    except :
        return

    if len(Application.objects.filter(app_name=appName)) == 0:
        ap = Application(app_name=appName, app_package=packageName)
        ap.save()
    else :
        ap = Application.objects.filter(app_name = appName)[0]

    cursor.execute("select _SOURCE_GEOMETRY, _BASETARGET, _EXPIREDDATE from T_BLE")
    while True :
        data = cursor.fetchone()
        if data == None :
            break
        #{"type":"Point","coordinates":[126.93271694,36.77677689,0]}
        loc = util.findAll(data[0], "[0-9.]+")
        try :
            lat = loc[0]
            lng = loc[1]
        except :
            continue
        #{"targetId":"29249132","type":"MID","targetName":"GS25 순천향학사"}
        name = util.findAll(data[1], "\"targetName\":\"(.+?)\"")[0]
        date = data[2]
        input_data = WayPoint(position = name,
                              position_x = lng,
                              position_y = lat,
                              point_time = date,
                              app_name_id = ap.id)
        input_data.save()

def Beadaltong_ab(appName, packageName, path, target) :
    try :
        con    = dbutil.appdbconnect(packageName, path, target)
        cursor = con.cursor()
    except :
        return

    ap = Application(app_name = appName, app_package = packageName)
    ap.save()

    cursor.execute("select event_data, timestamp from ab_events where event_type = 'lr'")
    while True :
        data = cursor.fetchone()
        if data == None :
            break
        #{"latitude":36.7293028,"longitude":127.0098995,"altitude":0,"ll_accuracy":25}
        loc = util.findAll(data[0], "[0-9.]+")
        try:
            lat = loc[0]
            lng = loc[1]
        except :
            continue
        input_data = WayPoint(position_x = lng,
                              position_y = lat,
                              app_name_id = ap.id)
        input_data.save()
