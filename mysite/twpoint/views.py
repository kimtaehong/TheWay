from django.shortcuts import render, get_object_or_404
from .models import WayPoint, Application, BaseStation
from django.utils import timezone


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

