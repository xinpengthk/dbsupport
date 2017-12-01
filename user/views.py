# -*- coding: UTF-8 -*- 

from collections import OrderedDict
import json
import multiprocessing
import re
import time

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from utils.aesDecryptor import Prpcrypt



# from .aes_decryptor import Prpcrypt
# from .const import Const
# from .dao import Dao
# from .inception import InceptionDao
# from .models import users, master_config, workflow
# from .sendmail import MailSender
prpCryptor = Prpcrypt()

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    if request.session.get('login_username', False):
        del request.session['login_username']
    return render(request, 'user/login.html')

def loginSuccessful(request):
    return render(request, 'base/main.html')

def changePasswd(request):
    return render(request, 'user/changePasswd.html')