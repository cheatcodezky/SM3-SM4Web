# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import File
from .models import User
from .common import *
from .SM4 import *

import random
# Create your views here.

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")
@csrf_exempt
def registerBehavior(request):
    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        pastAccount =  User.objects.filter(account=account)
        if(pastAccount.__len__() == 0):
            User.objects.create(account=account,password=password)
            return HttpResponse("200")
        else:
            return HttpResponse("444")
    else:
        return HttpResponse("404")
@csrf_exempt
def loginBehavior(request):
    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        tmpAccount = account.upper()
        key = ""
        for i in tmpAccount:
            tmpChar = ""
            if i > 'F':
                dValue = (ord(i)-ord('F'))%16-1
                if dValue < 10:
                    tmpChar = chr(dValue+ord('0'))
                else:
                    tmpChar = chr(dValue - 10 + ord('A'))
            else:
                tmpChar = i
            print("char : "+ tmpChar)
            key = key + tmpChar
        if key.__len__() > 32:
            key = key[0:32]
        else:
            tmpKey = key
            for i in range(key.__len__(),32):
                tmpKey = tmpKey + str('0')
            key = tmpKey
        sm4 = SM4(key= key)
        # print("password : ",password)
        M = sm4.sm4_decrypt(password, SM4_ECB)
        # print(M)
        password = M
        pastAccount =  User.objects.filter(account=account)
        if(pastAccount.__len__() == 0):
            return HttpResponse("444")
        else:
            accountM = sm4.sm4_decrypt(pastAccount[0].password, SM4_ECB)
            if(password == accountM):
                return HttpResponse("/contentPage/")
            else:
                return HttpResponse("445")
    else:
        return HttpResponse("404")
import random
import datetime
def contentPage(request):
    return render(request,'content.html')

import os
@csrf_exempt
def downloadFile(request):
    if request.method == 'POST':
        code = request.POST['code']
        searchResult =  File.objects.filter(code=code)
        if(searchResult.__len__() == 0):
            return HttpResponse('404')
        else:
            for i in searchResult:
                path = i.file.__str__()
                tmp  = path.split('/')
                result = "/".join(tmp[1:])
                result = "/"+result
                # print(result)
                # result = r"c:\fciv.exe"
                # print(os.listdir("."))
                message = {"url":result,"hashHex":i.hashHex}
                return JsonResponse(message)
                # return HttpResponse(result)
    else:
        return HttpResponse("404")


from .sm3 import *
@csrf_exempt
def saveFile(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        # print(int(file_obj.read[0]))
        # print((file_obj.read()[0]))

        # print(str(file_obj.read(),encoding='GBK',errors='backslashreplace'))
        read = file_obj.read()
        binaryFile = ""
        for i in read:
            binaryFile = binaryFile + bin(i)[2:]

        hashMsg = hash_msg(binaryFile)
        outHex = out_hex(hashMsg)
        if outHex != request.POST['haxhHex']:
            return HttpResponse('444')

        randomCode = random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789',5)
        code = ""
        for i in randomCode:
            code = code + i
        File.objects.create(code=code,hashHex=request.POST['haxhHex'],file=file_obj)
        return HttpResponse(code)
    else:
        return HttpResponse("404")
#'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'