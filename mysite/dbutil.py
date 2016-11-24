import sqlite3
import util

#############################################
################### SETUP ###################
#############################################

def connect() :
   return sqlite3.connect('./db.sqlite3')

def makeDB() :
   con = connect()
   cursor = con.cursor()

   #Make Table
   cursor.execute("CREATE TABLE picture(name varchar(255), path varchar(255), time int, device varchar(255), long real, lat real, md5 varchar(32), sha1 varchar(40));")
   cursor.execute("CREATE TABLE data(appName varchar(255), packageName   varchar(255), path varchar(255), tableName varchar(255), time varchar(255), position varchar(255), positionX varchar(255), positionY varchar(255), start varchar(255), startX varchar(255), startY varchar(255), end varchar(255), endX varchar(255), endY varchar(255), search varchar(255), searchX varchar(255), searchY varchar(255));")
   cursor.execute("CREATE TABLE bs(time int, long real, lat real, sender char(255), reciver char(255), location char(255), type char(255));")
   con.commit()
   con.close()

#############################################
#################### ING ####################
#############################################

################# CONNECT ###################

def inputResDB(insertQuery) :
   con = connect()
   cursor = con.cursor()
   cursor.execute(insertQuery)
   con.commit()
   con.close()

def appdata() :
   return sqlite3.connect('./appinfo.db')

def appdbconnect(packageName, path) :
   return sqlite3.connect('./phone/data/' + packageName + '/' + path)

################## GEN #####################

def appQuery(appInfo, appRecord, values) :
   query = 'insert into data(appName, packageName, path, tableName, '
   for i in values :
      query = query + i + ", "
   query = query [:-2] + ") values('%s', '%s', '%s', '%s', " %(appInfo['appName'], appInfo['packageName'], appInfo['path'], appInfo['tableName'])
   for i in appRecord :
      query = query + "'%s'," %util.toString(i).replace(u'\'', u'')
   query = query[:-1] + ');'
   return query

def genQuery(record) :
   query = "select "
   values = []
   print('record')
   for i in record.keys()[4:-1] :
      query = query + record[i] + ","
      values.append(i)
   return query[ :-1] + ' from ' + record['tableName'], values

################# Insert ###################

def writeImageData(name, path, time, device, long, lat, md5, sha1) :
   con = connect()
   cursor = con.cursor()
   #insert data
   cursor.execute("INSERT INTO picture VALUES ('%s', '%s', %d, '%s', %0.6lf, %0.6lf, '%s', '%s');" %(name, path, time, device, long, lat, md5, sha1))
   con.commit()
   con.close()

#############################################
#################### END ####################
#############################################

def appDataCount() :
   con = connect()
   cursor = con.cursor()
   cursor.execute("select count(*) from data;")
   count = cursor.fetchone()
   con.close()
   return count[0]

def picCount() :
   con = connect()
   cursor = con.cursor()
   cursor.execute("select count(*) from picture;")
   count = cursor.fetchone()
   con.close()
   return count[0]

#############################################
################### PHONE ###################
#############################################

#CREATE TABLE bs(time int, long real, rat real, sender char(255), reciver char(255), Type char(255));

def insertBSData(time, long, lat, sender, reciver, location, type) :
   con = connect()
   cursor = con.cursor()
   cursor.execute("insert into bs values(%d, %0.6f, %0.6f, '%s', '%s', '%s', '%s');" %(time, float(long), float(lat), sender, reciver, location, type))
   con.commit()
   return True

def bsQuery(rowData) :
   if 'position' not in rowData.keys() :
      return False
   if len(rowData['position']) == 4 or len(rowData['position']) == 0 :
      return False
   time = util.timeTotimestamp(rowData['time'])
   lat, lon = util.locToCoord(rowData['position'])
   if 'sender' not in rowData :
      rowData['sender'] = 'None'
   if 'reciver' not in rowData :
      rowData['reciver'] = 'None'

   insertBSData(time, lat, lon, rowData['sender'], rowData['reciver'], rowData['position'], rowData['type'])