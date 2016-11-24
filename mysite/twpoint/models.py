from django.db import models

# Example Model
class Application(models.Model):
    """어플리케이션 정보에 관한 모델"""
    app_name = models.CharField('Application Name', max_length=200)
    app_data_path = models.CharField('Data Path', max_length=200)

    def __str__(self):
        return self.app_name

    def dic(self):
        fields = ['id', 'app_name', 'app_data_path']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


# Example Model
class WayPoint(models.Model):
    """위치 정보에 관한 모델"""
    app_name = models.ForeignKey(Application, on_delete=models.CASCADE)
    point_name = models.CharField('Point Name',max_length=32)
    point_lat = models.FloatField('Point Latitude')
    point_lng = models.FloatField('Point Longitude')
    point_time = models.DateTimeField('Point Time', auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.point_name

    def GetPoint(self):
        """위도와 경도를 한번에 표시"""
        return str(self.point_lat) + ',' + str(self.point_lng)

    def dic(self):
        fields = ['id', 'app_name_id', 'point_name', 'point_lat', 'point_lng']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result


class BaseStation(models.Model):
    name = models.CharField('Name', max_length=200)
    lat = models.FloatField('Latitude')
    lng = models.FloatField('Longitude')

    def __str__(self):
        return self.name


# waypoint 추가 사항
# start point, end point
# 검색한 내용인지, 실질적 내용인지 확인
