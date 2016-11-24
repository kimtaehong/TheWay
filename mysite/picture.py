import dbutil
import exifread
import gpsutil
import util
import os

def getEXIFDevice(tags) :
	if 'Image Model' in tags :
		return tags['Image Model']
	return None

def pictureGPS(name, path) :
	f = open(path + '/' + name, 'rb')

	tags = util.retTags(f)
	if tags == {} :
		return False

	file = f.read()

	x, y = gpsutil.get_exif_location(tags)
	if x == None or y == None :
		return False

	device = getEXIFDevice(tags)
	
	try :
		time = util.tag2timestamp(tags['EXIF DateTimeOriginal'])
	except :
		time = 0

	md5  = util.md5(file)
	sha1 = util.sha1(file)
	dbutil.writeImageData(name, path, time, device, x, y, md5, sha1)
	return True

def picture_search(dir) :
	dirlist = os.listdir(dir)
	for i in dirlist :
		if os.path.islink(dir+"/"+i) == True :
			pass
		elif os.path.isdir(dir+"/"+i) == True :
			picture_search(dir+"/"+i)
		else :
			location = dir + "/" + i
			location = location.replace("//", "/")
			ext      = os.path.splitext(dir+"/"+i)[-1].lower()
			if ext == '.jpg' :
				pictureGPS(i, dir)