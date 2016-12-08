from django.db import models


class Application(models.Model):
    """어플리케이션 정보에 관한 모델"""
    app_name = models.CharField('Application Name', max_length=200)
    app_package = models.CharField('Data Path', max_length=200)

    def __str__(self):
        return self.app_name

    def dic(self):
        fields = ['id', 'app_name', 'app_package']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class WayPoint(models.Model):
    """위치 정보에 관한 모델"""
    app_name   = models.ForeignKey(Application, on_delete=models.CASCADE)
    path       = models.CharField(max_length=255, null=True)
    table_name = models.CharField(max_length=255, null=True)
    point_time = models.CharField(max_length=255, null=True)
    position   = models.CharField(max_length=255, null=True)
    position_x = models.CharField(max_length=255, null=True)
    position_y = models.CharField(max_length=255, null=True)
    start      = models.CharField(max_length=255, null=True)
    start_x    = models.CharField(max_length=255, null=True)
    start_y    = models.CharField(max_length=255, null=True)
    end        = models.CharField(max_length=255, null=True)
    end_x      = models.CharField(max_length=255, null=True)
    end_y      = models.CharField(max_length=255, null=True)
    search     = models.CharField(max_length=255, null=True)
    search_x   = models.CharField(max_length=255, null=True)
    search_y   = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.position is not None:
            return self.position
        elif self.start is not None:
            return self.start + "," + self.end
        elif self.search is not None:
            return self.search
        else:
            return "WayPoint_model"

    def dic(self):
        fields = [
            'id',
            'app_name_id',
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
            'search_y'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class Picture(models.Model):
    name   = models.CharField(max_length=255)
    path   = models.CharField(max_length=255)
    time   = models.IntegerField()
    device = models.CharField(max_length=255)
    lng    = models.FloatField()
    lat    = models.FloatField()
    sha1   = models.CharField(max_length=40)
    md5    = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def dic(self):
        fields = [
            'id',
            'name',
            'path',
            'device',
            'lng',
            'lat',
            'md5',
            'sha1'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class BaseStation(models.Model):
    time     = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lat      = models.FloatField('Latitude')
    lng      = models.FloatField('Longitude')
    sender   = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    type     = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def dic(self):
        fields = [
            'id',
            'time',
            'location',
            'lat',
            'lng',
            'sender',
            'receiver',
            'type'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class UserInfo(models.Model):
    name        = models.CharField(max_length=50)
    case_no     = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class statics(models.Model):
    name  = models.CharField(max_length=50)
    count = models.IntegerField()
    level = models.IntegerField() #Level -> 서울시 => lv1, 강남구 => Lv2
    pid   = models.IntegerField() #parent ID

    def __str__(self):
            return "statics"

    def dic(self):
        fields = [
            'name',
            'count',
            'level',
            'pid'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result
