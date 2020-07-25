from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.now()
    if today.day == 31 and today.month == 12:
        s = "yes, it's new years!"
    else:
        s = "no :("
    return render(request, "index.html", {
        "s": s
    })
