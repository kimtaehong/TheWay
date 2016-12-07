from django.shortcuts import render, get_object_or_404, HttpResponse, render_to_response
from .models import WayPoint, Application, BaseStation, Picture, UserInfo
from django.utils import timezone
import json
import bsparser
import app
import picture
from django.views.decorators.csrf import csrf_exempt
import os
import pdb


@csrf_exempt
def index(request):
    """index page"""
    app_model = Application.objects.all()
    way_model = WayPoint.objects.all()
    user_model = UserInfo.objects.all()
    bs_model = BaseStation.objects.all()
    picture_model = Picture.objects.all()
    # db clear

    bs_model.delete()
    picture_model.delete()
    user_model.delete()
    app_model.delete()
    way_model.delete()

    return render(request, 'twpoint/index.html', {"time": timezone.localtime(timezone.now()), })


def detail(request, application_id):
    """detail page"""
    app = get_object_or_404(Application, pk=application_id)    # 선택한 applciation의 해당하는 data
    applications = Application.objects.all()
    bs = BaseStation.objects.all()
    user = UserInfo.objects.first()

    context = {
        'time': timezone.localtime(timezone.now()),
        'app': app,
        'application': applications,      # header.html 에서 application 목록을 출력
        'BaseStation': bs,
        'user': user,
    }
    return render(request, 'twpoint/detail.html', context)


def result(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            bsparser.parse(request.FILES['file'].name, request.FILES['file'].read().decode('utf-8'))

    applications = Application.objects.all()
    user = UserInfo.objects.first()
    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
        'user': user,
    }
    return render(request, 'twpoint/result.html', context)


def gallery(request):
    applications = Application.objects.all()
    user = UserInfo.objects.all()
    pictures = Picture.objects.all()

    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
        'user': user,
        'pictures': pictures,
    }
    return render(request, 'twpoint/gallery.html', context)


def parsing(request):
    picture.picture_search('./' + request.POST['filename'])
    app.appdata('./'+request.POST['filename'])
    # db.sqlite3안에 data table, picture table에 값을 가져오는 코드 필요...
    post_user = UserInfo()
    post_user.name = request.POST['Name']
    post_user.case_no = request.POST['Case_no']
    post_user.description = request.POST['Description']
    post_user.save()

    user = UserInfo.objects.first()

    context = {
        'user': user
    }
    return render_to_response('twpoint/parsing.html', context)


def base_station(request):
    applications = Application.objects.all()
    user = UserInfo.objects.all()
    stations = BaseStation.objects.all()

    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
        'user': user,
        'stations': stations,
    }

    return render(request, 'twpoint/basestation.html', context)


def distribution(request):
    applications = Application.objects.all()
    user = UserInfo.objects.all()
    waypoints = WayPoint.objects.all()

    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
        'user': user,
        'waypoints': waypoints
    }

    return render(request, 'twpoint/distribution.html', context)


# Data View By JSON
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


def pictureview(request):
    """ /picture picture 정보"""
    picture_data = Picture.objects.all()
    data = []
    for pic in picture_data:
        data.append(pic.dic())

    return HttpResponse(json.dumps(data), content_type="application/json")


def basestationview(request):
    """ /basestation basestation 정보"""
    base_data = BaseStation.objects.all()
    data = []
    for bs in base_data:
        data.append(bs.dic())

    return HttpResponse(json.dumps(data), content_type='application/json')


def image(request):
    file = open(request.GET['file'], 'rb').read()
    return HttpResponse(file, content_type="image/jpeg")
