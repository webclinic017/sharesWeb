import time
import thread
import sqlite3
import django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from googleFinance import getShare
from sharesWebApp.models import Share

def inicio(request, notifMsg=''):
    sh = Share.objects.all()[2]
    company = sh.ticker
    share = getShare(company)
    values = share
    return render(request, 'inicio.html', values)