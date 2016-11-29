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
    app_name = models.ForeignKey(Application, on_delete=models.CASCADE)
    point_time = models.DateTimeField('Point Time', auto_now=False, auto_now_add=False, null=True)
    position = models.CharField(max_length=255, null=True)
    position_x = models.CharField(max_length=255, null=True)
    position_y = models.CharField(max_length=255, null=True)
    start = models.CharField(max_length=255, null=True)
    start_x = models.CharField(max_length=255, null=True)
    start_y = models.CharField(max_length=255, null=True)
    end = models.CharField(max_length=255, null=True)
    end_x = models.CharField(max_length=255, null=True)
    end_y = models.CharField(max_length=255, null=True)
    search = models.CharField(max_length=255, null=True)
    search_x = models.CharField(max_length=255, null=True)
    search_y = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.position is not None:
            return self.position
        if self.start is not None:
            return self.start + "," + self.end
        if self.search is not None:
            return self.search

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
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    time = models.IntegerField()
    device = models.CharField(max_length=255)
    lng = models.FloatField()
    lat = models.FloatField()
    md5 = models.CharField(max_length=32)
    sha1 = models.CharField(max_length=40)

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
    time = models.IntegerField()
    location = models.CharField(max_length=255)
    lat = models.FloatField('Latitude')
    lng = models.FloatField('Longitude')
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

