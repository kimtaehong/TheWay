from django.shortcuts import render, get_object_or_404, HttpResponse, render_to_response
from .models import WayPoint, Application, BaseStation, Picture
from django.utils import timezone
import json
import bsparser
import app
import picture
from django.views.decorators.csrf import csrf_exempt
import pdb



@csrf_exempt
def index(request):
    """index page"""
    app_model = Application.objects.all()
    way_model = WayPoint.objects.all()
    bs_model = BaseStation.objects.all()
    picture_model = Picture.objects.all()

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
    if request.method == 'POST':
        if 'file' in request.FILES:
            bsparser.parse(request.FILES['file'].name, request.FILES['file'].read().decode('utf-8'))

    applications = Application.objects.all()
    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications
    }
    return render(request, 'twpoint/result.html', context)


def gallery(request):
    applications = Application.objects.all()
    context = {
        'time': timezone.localtime(timezone.now()),
        'application': applications,
    }
    return render(request, 'twpoint/gallery.html', context)


def parsing(request):
    picture.picture_search('./' + request.POST['filename'])
    app.appdata('./'+request.POST['filename'])
    # db.sqlite3안에 data table, picture table에 값을 가져오는 코드 필요...
    context = {
            'Name': request.POST['Name'],
            'Case_no': request.POST['Case_no'],
            'Description': request.POST['Description']
    }
    return render_to_response('twpoint/parsing.html', context)


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
