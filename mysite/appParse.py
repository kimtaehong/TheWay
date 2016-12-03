import dbutil
from twpoint.models import Application, WayPoint
import pdb

def Parse(appName, packageName, path, tableName, target):
    if appName == 'appA' and path == 'fileA' :
        return appA_fileA(appName, packageName, path)
    elif appName == 'cymera' and path == 'databases/cymeraGallery.db' :
        return cymera_cymeraGallery(appName, packageName, path, target)


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
        lng = data[0]
        lat  = data[1]
        input_data = WayPoint(path = path, table_name = 'cymera_photos, cymera_exif', position_x = lng, position_y = lat, app_name_id = ap.id)
        input_data.save()
