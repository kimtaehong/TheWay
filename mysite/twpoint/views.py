from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import WayPoint, Application, BaseStation
from django.utils import timezone
import json


def index(request):
    """index page"""
    return render(request, 'twpoint/index.html', {"time": timezone.localtime(timezone.now()), })


def detail(request, application_id):
    """detail page"""
    app = get_object_or_404(Application, pk=application_id)    # 선택한 applciation의 해당하는 data
    applications = Application.objects.all()
    bs = BaseStation.objects.all()
    context = {
        'time': timezone.localtime(timezone.now()),
        'app': app,
        'application': applications,      # header.html 에서 application 목록을 출력
        'BaseStation': bs,
    }
    return render(request, 'twpoint/detail.html', context)


def result(request):
    applications = Application.objects.all()
    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
    }
    return render(request, 'twpoint/result.html', context)


def gallery(request):
    applications = Application.objects.all()
    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
    }
    return render(request, 'twpoint/gallery.html', context )


def parsing(request):
    return render(request, 'twpoint/parsing.html', {"time": timezone.localtime(timezone.now()), })
# data view


def dataview(request):
    """/application application 정보"""
    app_data = Application.objects.all()
    data = []
    for app in app_data:
        data.append(app.dic())
    return HttpResponse(json.dumps(data), content_type="application/json")


def wayview(request):
    """/waypoint waypoint 정보"""
    waypoint_data = WayPoint.objects.all()
    data = []
    for wp in waypoint_data:
        data.append(wp.dic())
    return HttpResponse(json.dumps(data), content_type="application/json")


def wayviewbyapp(request, application_id):
    """/waypoint/... application의 id에 따른 waypoint 정보"""
    wpapp = WayPoint.objects.all()
    data = []
    for wp in wpapp:
        if wp.dic()['app_name_id'] == int(application_id):
            data.append(wp.dic())
    return HttpResponse(json.dumps(data), content_type="application/json")
