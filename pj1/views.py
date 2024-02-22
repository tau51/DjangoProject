import builtins
import datetime
import json

from django import db
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from pj1 import models


# 初始界面
def index(request):
    return render(request, "login.html")


# 注册功能
def sign(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.user.objects.filter(username=username)
        if len(user_obj) == 0 and username != "" and password != '':
            models.user.objects.create(username=username, password=password)
            messages.success(request, '注册成功')
            return HttpResponseRedirect("/index/")
    except Exception as e:
        if type(e) is db.utils.IntegrityError:
            return HttpResponse("用户名已被使用")
    messages.error(request, '注册失败')
    return HttpResponseRedirect("/sign/")


# 注册界面
def signup(request):
    return render(request, "sign.html")


# 登陆功能
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.user.objects.filter(username=username, password=password, deleted=False)
        if not user_obj:
            messages.error(request, '用户名或密码不正确')
            return HttpResponseRedirect('/index/')
        else:
            request.session['username'] = username
            return HttpResponseRedirect('/clue/')


# 获取信息
def clue(request):
    if request.method == 'GET':
        context = {}
        username = request.session.get('username')
        context['username'] = username
        return render(request, 'clue.html', context)
    else:
        data = []
        clue_obj = models.clue.objects.all()
        for clue in clue_obj:
            if clue.deleted is True:
                continue
            context = {'id': clue.id,
                       'username': clue.username,
                       'province': clue.province,
                       'city': clue.city,
                       'club': clue.club,
                       'link': clue.link,
                       'fans': clue.fans,
                       'type': clue.type,
                       'wechat': clue.wechat,
                       'group': clue.group,
                       'audits': clue.audits,
                       'settle': clue.settle,
                       'status': clue.status}
            data.append(context)
        return JsonResponse(data, safe=False)


# 查看我的信息
def clue_mine(request):
    data = list()
    username = request.session.get('username')
    clue_obj = models.clue.objects.filter(username=username)
    for clues in clue_obj:
        if clues.deleted is True:
            continue
        context = {'id': clues.id,
                   'username': clues.username,
                   'province': clues.province,
                   'city': clues.city,
                   'club': clues.club,
                   'link': clues.link,
                   'fans': clues.fans,
                   'type': clues.type,
                   'wechat': clues.wechat,
                   'group': clues.group}
        data.append(context)
    return JsonResponse(data, safe=False)


# 编辑信息
def edit_clue(request):
    data = json.loads(request.body)
    username = data['username']
    province = data['province']
    city = data['city']
    club = data['club']
    link = data['link']
    fans = data['fans']
    type = data['type']
    wechat = data['wechat']
    group = data['group']
    id = data['id']
    clue_obj = models.clue.objects.filter(id=id)
    if len(clue_obj) != 0:
        try:
            clue_obj.update(username=username, province=province, city=city, link=link, fans=fans, type=type,
                            group=group, club=club, wechat=wechat, update_time=timezone.localtime(timezone.now()))
            return HttpResponse("修改成功")
        except Exception as e:
            if type(e) is db.utils.IntegrityError:
                return HttpResponse("微信号/俱乐部名称已被使用")
            else:
                return HttpResponse("修改失败")
    else:
        return HttpResponse("修改失败")


# 新增信息
def add_clue(request):
    data = json.loads(request.body)
    username = data['username']
    province = data['province']
    city = data['city']
    club = data['club']
    link = data['link']
    fans = data['fans']
    type = data['type']
    wechat = data['wechat']
    group = data['group']
    try:
        models.clue.objects.create(username=username, province=province, city=city, link=link, fans=fans, type=type,
                                   group=group, club=club, wechat=wechat,
                                   update_time=timezone.localtime(timezone.now()))
        return HttpResponse("新增成功")
    except Exception as e:
        if builtins.type(e) is db.utils.IntegrityError:
            return HttpResponse("微信号/俱乐部已被使用")
        else:
            return HttpResponse("新增失败")


# 删除信息
def delete_clue(request):
    username = request.session.get('username')
    data = json.loads(request.body)
    id = data['id']
    clue_obj = models.clue.objects.filter(id=id)
    print(clue_obj[0].username)
    if clue_obj[0].username == username:
        try:
            clue_obj.update(deleted=True, update_time=datetime.datetime.now())
            return HttpResponse("已删除")
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("删除失败")


# 管理员界面
def admin(request):
    return render(request, 'admin.html')


# 管理员查看信息
def clue_admin(request):
    data = []
    clue_obj = models.clue.objects.all()
    for clue in clue_obj:
        if clue.deleted is True:
            continue
        context = {}
        context['id'] = clue.id
        context['username'] = clue.username
        context['province'] = clue.province
        context['city'] = clue.city
        context['club'] = clue.club
        context['link'] = clue.link
        context['fans'] = clue.fans
        context['type'] = clue.type
        context['wechat'] = clue.wechat
        context['group'] = clue.group
        context['audits'] = clue.audits
        context['settle'] = clue.settle
        context['status'] = clue.status
        data.append(context)
    return JsonResponse(data, safe=False)


# 管理员编辑信息
def edit_clue_admin(request):
    data = json.loads(request.body)
    print(data)
    id = data['id']
    username = data['username']
    province = data['province']
    city = data['city']
    club = data['club']
    link = data['link']
    fans = data['fans']
    type = data['type']
    wechat = data['wechat']
    group = data['group']
    clue_obj = models.clue.objects.filter(username=username, id=id)
    if len(clue_obj) != 0:
        try:
            clue_obj.update(username=username, province=province, city=city, link=link, fans=fans, type=type,
                            group=group, club=club, wechat=wechat, update_time=timezone.localtime(timezone.now()))
            return HttpResponse("修改成功")
        except Exception as e:
            if type(e) == db.utils.IntegrityError:
                return HttpResponse("微信号/俱乐部名已被使用")
            else:
                return HttpResponse("修改失败")


# 管理员删除信息
def delete_clue_admin(request):
    data = json.loads(request.body)
    id = data['id']
    clue_obj = models.clue.objects.filter(id=id)
    clue_obj.update(deleted=True, update_time=timezone.localtime(timezone.now()))
    return HttpResponse("已删除")


# 账户管理界面
def user_admin_check(request):
    return render(request, 'useradmin.html')


# 管理员获取账户信息
def user_admin(request):
    data = []
    user_obj = models.user.objects.all()
    for users in user_obj:
        if users.deleted is True:
            continue
        context = {'id': users.id, 'username': users.username, 'password': users.password}
        data.append(context)
    return JsonResponse(data, safe=False)


# 管理员修改账户
def edit_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        id = data['id']
        user_obj = models.user.objects.filter(id=id)
        old_username = user_obj.first().username
        clue_obj = models.clue.objects.filter(username=old_username, deleted=False)
        try:
            clue_obj.update(username=username, update_time=timezone.localtime(timezone.now()))
        except Exception as e:
            print(e)
        if len(user_obj) != 0:
            try:
                user_obj.update(username=username, password=password, id=id,
                                update_time=timezone.localtime(timezone.now()))
                return HttpResponse("修改成功")
            except Exception as e:
                if type(e) == db.utils.IntegrityError:
                    return HttpResponse("微信号已被使用")
                else:
                    return HttpResponse("修改失败")


# 管理员删除账户
def delete_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        user_obj = models.user.objects.filter(username=username)
        user_obj.update(deleted=True, update_time=timezone.localtime(timezone.now()))
        clue_obj = models.clue.objects.filter(username=username)
        clue_obj.update(deleted=True, update_time=timezone.localtime(timezone.now()))
        return HttpResponse("已删除")


# 上传csv
def clue_load(request):
    if request.method == 'POST':
        clues = json.loads(request.body)
        ja = json.loads(clues)[1:]
        print(ja)
        try:
            with transaction.atomic():
                for data in ja:
                    if data['username'] == '' or data['username'] == '用户名':
                        continue
                    username = data['username']
                    province = data['province']
                    city = data['city']
                    club = data['club']
                    link = data['link']
                    fans = data['fans']
                    type = data['type']
                    wechat = data['wechat']
                    group = data['group']
                    audits = data['audits']
                    settle = data['settle']
                    status = data['status']
                    models.clue.objects.create(username=username, province=province, city=city, link=link, fans=fans,
                                               type=type, group=group, club=club, wechat=wechat, audits=audits,
                                               settle=settle, status=status)
                    user_obj = models.user.objects.filter(username=username)
                    if len(user_obj) == 0:
                        models.user.objects.create(username=username, password=123456)
                return HttpResponse("导入成功")
        except Exception as e:
            return HttpResponse(e)


# 审核、结算、状态的编辑功能
def manage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data['id']
        username = data['username']
        province = data['province']
        city = data['city']
        club = data['club']
        link = data['link']
        fans = data['fans']
        type = data['type']
        wechat = data['wechat']
        group = data['group']
        audits = data['audits']
        settle = data['settle']
        status = data['status']
        clue_obj = models.clue.objects.filter(id=id)
        try:
            clue_obj.update(audits=audits, settle=settle, status=status, update_time=timezone.localtime(timezone.now()))
            return HttpResponse("修改成功")
        except Exception as e:
            return HttpResponse(e)
