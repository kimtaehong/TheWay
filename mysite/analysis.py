import util
import dbutil
from twpoint.models import Application, WayPoint, statics


def static():
    datas = WayPoint.objects.all()
    for data in datas:
        if util.isNotNone(data.start_x, data.start_y):
            dbutil.input(data.start_x, data.start_y)
        if util.isNotNone(data.end_x, data.end_y):
            dbutil.input(data.end_x, data.end_y)
        if util.isNotNone(data.position_x, data.position_y):
            dbutil.input(data.position_x, data.position_y)
        if util.isNotNone(data.search_x, data.search_y):
            dbutil.input(data.search_x, data.search_y)
