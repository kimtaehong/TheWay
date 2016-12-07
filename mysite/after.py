from twpoint.models import Application, WayPoint

def process(function, id) :
    if function == 'blank' :
        blank(id)
    if function == 'NikeRun' :
        NikeRun(id)

def blank(id) :
    #this is blank
    pass

def NikeRun(id) :
    pass
