import dbutil
import exifread
import gpsutil
import util
from twpoint.models import Picture
import os


def getEXIFDevice(tags):
    if 'Image Model' in tags:
        return tags['Image Model']
    return None


def pictureGPS(name, path):
    f = open(path + '/' + name, 'rb')
    path=path[2:]
    tags = util.retTags(f)
    if tags == {}:
        return False

    file = f.read()

    x, y = gpsutil.get_exif_location(tags)
    if x is None or y is None:
        return False

    device = getEXIFDevice(tags)
    try:
        time = util.tag2timestamp(tags['EXIF DateTimeOriginal'])
    except:
        time = 0

    md5 = util.md5(file)
    sha1 = util.sha1(file)
    # dbutil.writeImageData(name, path, time, device, x, y, md5, sha1)
    pic = Picture(name = name,
                  path = path,
                  time = time,
                  device = device,
                  lat = x,
                  lng = y,
                  md5 = md5,
                  sha1 = sha1)
    pic.save()
    return True


def picture_search(dir):
    dirlist = os.listdir(dir)
    for i in dirlist :
        if os.path.islink(dir+"/"+i) is True :
            pass
        elif os.path.isdir(dir+"/"+i) is True :
            picture_search(dir+"/"+i)
        else :
            location = dir + "/" + i
            location = location.replace("//", "/")
            ext = os.path.splitext(dir+"/"+i)[-1].lower()
            if ext == '.jpg' :
                pictureGPS(i, dir)
