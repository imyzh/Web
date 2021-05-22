from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from app1.jwt_auth import create_token,parse_payload,JwtAuthentication
from app1.models import userinfo,historyevent

class index(APIView):
    def get(self,request,format=None):
        res = {'data': None, 'error': None}
        user = {'name': "yzh", 'pswd': "123"}
        try:
            name = request.GET.get('username')
            print(name)
            res['data'] = str(user)
            res['error'] = "admin"
        except:
            pass
        return JsonResponse(res, json_dumps_params={'ensure_ascii':False})
    def post(self,request,format=None):
        try:
            name = request.data['username']
            print(name)
        except:
            pass
        result = {'res':'res'}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

class Historyeventinfo(APIView):
    # 视频历史事件
    def get(self,request,format=None):
        res = {'data': None, 'error': None}
        info={}
        infolist={}
        try:
            devid = request.data['devid']
            if devid == 'ALL':
                outall = historyevent.objects.all()
                for var in outall:
                    infolist[str(var)] = {
                        'maskinfo':var.maskinfo,
                        'evtime':var.evtime,
                        'hashcode':var.hashcode,
                        'level':var.level,
                        'des':var.des
                    }
                info = infolist
            else:
                out = historyevent.objects.filter(devid=devid).first()
                if out is not None:
                    infolist[str(out)] = {
                        'maskinfo':out.maskinfo,
                        'evtime':out.evtime,
                        'hashcode':out.hashcode,
                        'level': out.level,
                        'des':out.des
                    }
                    info = infolist
                else:
                    info = None
            res['data'] = info
        except:
            res['error'] = '格式错误'
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})


class Realtimeeventinfo(APIView):
    # 视频实时事件
    def get(self,request,format=None):
        res = {'data': None, 'error': None}
        info={}
        infolist={}
        try:
            devid = request.data['devid']
            if devid == 'ALL':
                outall = historyevent.objects.all()
                for var in outall:
                    infolist[str(var)] = {
                        'maskinfo':var.maskinfo,
                        'evtime':var.evtime,
                        'hashcode':var.hashcode,
                        'level':var.level,
                        'des':var.des
                        
                    }
                info = infolist
            else:
                out = historyevent.objects.filter(devid=devid).first()
                if out is not None:
                    infolist[str(out)] = {
                        'maskinfo':out.maskinfo,
                        'evtime':out.evtime,
                        'hashcode':out.hashcode,
                        'level': out.level,
                        'des':out.des
                    }
                    info = infolist
                else:
                    info = None
            res['data'] = info
        except:
            res['error'] = '格式错误'
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})


class Login(APIView):
    # 登录
    def post(self,request,format=None):
        res = {'data': None, 'error': None}
        try:
            username = request.data['username']
            password = request.data['password']
            user = userinfo.objects.filter(name=username, pswd=password).first()
            if user is not None:
                payload = {'user':user.name,'power':user.power}
                token = {'token':create_token(payload)}
                res['data'] = token
            else:
                res['error'] = '登录失败'
        except:
            res['error'] = '格式错误'
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})


class UserAll(APIView):
    authentication_classes = [JwtAuthentication,]
    # 获取所有用户
    def get(self,request,format=None):
        res = {'data': None, 'error': None}
        if request.auth is None:
            if request.user['power'] == '0':
                username = ''
                userall = userinfo.objects.all()
                for var in userall:
                    username += (str(var.name)+';')
                userlist = {"user":username}
                res['data'] = userlist
            else:
                res['error'] = '权限不够'
        else:
            res = {'data': request.user, 'error': request.auth}
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})
    # 添加一个用户
    def post(self,request,format=None):
        res = {'data': None, 'error': None}
        try:
            power = request.data['power']
            username = request.data['username']
            password = request.data['password']
            if power == '0' or power == '1' or power == '2':
                if power == '2':
                    user = userinfo.objects.filter(name=username).first()
                    if user is None:
                        nuser = userinfo(name=username, pswd=password, power=power)
                        nuser.save()
                        payload = {'user':nuser.name,'power':nuser.power}
                        token = {'token':create_token(payload)}
                        res['data'] = token
                    else:
                        res['error'] = '用户已存在'
                else:
                    if request.auth is None and request.user['power'] == '0':
                        user = userinfo.objects.filter(name=username).first()
                        if user is None:
                            nuser = userinfo(name=username, pswd=password, power=power)
                            nuser.save()
                            payload = {'user':nuser.name,'power':nuser.power}
                            token = {'token':create_token(payload)}
                            res['data'] = token
                        else:
                            res['error'] = '用户已存在'
                    else:
                        res['error'] = '权限不够'
            else:
                res['error'] = '格式错误' 
        except:
            res['error'] = '格式错误'
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})


class UserInfo(APIView):
    authentication_classes = [JwtAuthentication,]
    # 查看一个用户
    def get(self,request,format=None):
        res = {'data': None, 'error': None}
        if request.auth is None:
            try:
                username = request.data['username']
                if request.user['power'] == '0':
                    username = userinfo.objects.filter(name=username).first()
                    if username is not None:
                        res['data'] = {
                            'name':username.name,
                            'pswd':username.pswd,
                            'power':username.power
                        }
                        pass
                    else:
                        res['error'] = '用户不存在'
                else:
                    res['error'] = '权限不够'
            except:
                res['error'] = '格式错误'
        else:
            res = {'data': request.user, 'error': request.auth}
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})
    # 修改当前用户信息
    def put(self,request,format=None):
        res = {'data': None, 'error': None}
        try:
            username = request.data['username']
            password = request.data['password']
            newusername = request.data['newusername']
            newpassword = request.data['newpassword']
            user = userinfo.objects.filter(name=username, pswd=password).first()
            if user is not None:    
                if user.power is not '2':
                    newuser = userinfo.objects.filter(name=newusername).first()
                    if newuser is None:
                        user.name = newusername
                        user.pswd = newpassword
                        user.save()
                    else:
                        res['error'] = '用户已存在'
                else:
                    res['error'] = '权限不够'
            else:
                res['error'] = '用户不存在'
        except:
            res['error'] = '格式错误'
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})
    # 超级管理用户信息
    def patch(self,request,format=None):
        res = {'data': None, 'error': None}
        if request.auth is None:
            try:
                username = request.data['username']
                newpower = request.data['newpower']
                newusername = request.data['newusername']
                newpassword = request.data['newpassword']
                if newpower is '0' or newpower is '1' or newpower is '2': 
                    if request.user['power'] == '0':
                        user = userinfo.objects.filter(name=username).first()
                        if user is not None: 
                            newuser = userinfo.objects.filter(name=newusername).first()
                            if newuser is None:
                                user.name = newusername
                                user.pswd = newpassword
                                user.power = newpower
                                user.save()
                            else:
                                res['error'] = '用户已存在'
                        else:
                            res['error'] = '用户不存在'
                    else:
                        res['error'] = '权限不够'
                else:
                    res['error'] = '格式错误'
            except:
                res['error'] = '格式错误'
        else:
            res = {'data': request.user, 'error': request.auth}
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})
    # 超级管理删除用户
    def delete(self,request,format=None):
        res = {'data': None, 'error': None}
        if request.auth is None:
            try:
                username = request.data['username']
                if request.user['power'] == '0':
                    user = userinfo.objects.filter(name=username).first()
                    if user is not None: 
                        user.delete()
                    else:
                        res['error'] = '用户不存在'
                else:
                    res['error'] = '权限不够'
            except:
                res['error'] = '格式错误'
        else:
            res = {'data': request.user, 'error': request.auth}
        result = {'res':res}
        return JsonResponse(result, json_dumps_params={'ensure_ascii':False})























# # from django.views import View
# # from rest_framework import status

# # from datetime import datetime

# from app1.models import UserInfo

# # from multiprocessing.pool import ThreadPool
# # from multiprocessing import cpu_count
# # from project.settings import MEDIA_ROOT
# # import os,json

# # # import jwt
# # import datetime
# # # from jwt import exceptions

# # import sys,os
# # sys.path.append(os.path.dirname(__file__) + os.sep + '../../')
# # # from tools.multi_task import detect15ClassDota
# # # from a import pa
# from rest_framework.authentication import BaseAuthentication

# from rest_framework import exceptions

# # # Create your views here.

# class AuthticationView(BaseAuthentication):
#     def authenticate(self,request):
#         try:
#             token = request.data['token']
#             user = UserInfo.objects.filter(token=token).first()
#             if not user:
#                 raise exceptions.AuthenticationFailed('认证失败')
#             else:
#                 return (user.username, user)
#         except:
#             pass
    
#     def authenticate_header(self, request):
#         pass

# class Order(APIView):
#     authentication_classes = [AuthticationView] 
#     def get(self,request,format=None):
#         result = {"res":'reslist',"token":'token'}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# # 登录
# class Login(APIView):
#     def post(self,request,format=None):
#         token   = 'None'
#         reslist = 'None'
#         try:
#             username = request.data['username']
#             password = request.data['password']
#             username = UserInfo.objects.filter(username=username, password=password).first()
#             if username is not None:
#                 token = str(uuid.uuid4())
#                 username.token = token
#                 username.save()
#             reslist = str(username)
#         except:
#             pass
#         result = {"res":reslist,"token":token}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# # 账号注册
# class Register(APIView):
#     def post(self,request,format=None):
#         token='NULL'
#         reslist = '校验码错误'
#         try:
#             token = request.data['token']
#             username = request.data['username']
#             password = request.data['password']
#             user = UserInfo.objects.filter(token=token).first()
#             if user is not None:
#                 user = UserInfo.objects.filter(username=username).first()
#                 if user is None:
#                     token = str(uuid.uuid4())
#                     username = UserInfo(username=username,password=password)
#                     username.token = token
#                     username.save()
#                     reslist = '账号创建成功'
#                 else:
#                     reslist = '账号存在'
#             else:
#                 reslist = '校验码错误'

#         except:
#             reslist = '数据格式错误!'
#         result = {"token":token, "results":reslist}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})



# # # 处理函数
# # class Order(APIView):
# #     def post(self,request,format=None):
# #         try:
# #             token = request.data['token']
# #             user = UserInfo.objects.filter(token=token).first() 
# #             if user is not None:
# #                 reslist = '下发任务'
# #             else:
# #                 reslist = '校验码错误'
# #         except:
# #             reslist = '数据格式错误!'
# #         result = {"results":reslist}
# #         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# # class debug1(APIView):
# #     def get(self,request,format=None):
# #         print(request.data)
# #         result = {"results":"OK"}
# #         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})


# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from app1.models import *
# # from app1.serializers import *

# # class UserView(APIView):
# #     def get(self,request,pk):
# #         user = UserInfo.objects.get(id=pk)
# #         user_ser = UserInfoSer(user)
# #         return Response(user_ser.data)

# 登录
# class Login(APIView):
#     def post(self,request,format=None):
#         token   = 'None'
#         reslist = 'None'
#         try:
#             username = request.data['username']
#             password = request.data['password']
#             username = UserInfo.objects.filter(username=username, password=password).first()
#             if username is not None:
#                 print(reslist)
#                 token = str(uuid.uuid4())
#                 username.token = token
#                 username.save()
#             reslist = str(username)
#         except:
#             pass
#         result = {"res":reslist,"token":token}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# # from jwt

# # 登录
# class jwtLogin(APIView):
#     authentication_classes = [JwtAuthentication,]
#     def post(self,request,format=None):
#         token   = 'None'
#         reslist = 'None'
#         try:
#             username = request.data['username']
#             password = request.data['password']
#             username = UserInfo.objects.filter(username=username, password=password).first()
#             if username is not None:
                
#                 # encoded_jwt = jwt.encode({'username':'运维咖啡吧','site':'https://ops-coffee.cn'},'secret_key',algorithm='HS256')
#                 # print(encoded_jwt)
#                 pass
#             reslist = str(username)
#         except:
#             pass
#         result = {"res":reslist,"token":token}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# class jwtOrder(APIView):
#     authentication_classes = [JwtAuthentication,]
#     def post(self,request,format=None):
#         token   = 'None'
#         reslist = 'None'
#         try:
#             username = request.data['username']
#             password = request.data['password']
#             username = UserInfo.objects.filter(username=username, password=password).first()
#             if username is not None:
#                 token = 'dsfadfad'
#             reslist = str(username)
#         except:
#             pass
#         result = {"res":reslist,"token":token}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# from app1.jwt_auth import create_token,parse_payload

# class jwtLogin(APIView):
#     def post(self,request,format=None):
#         token   = 'None'
#         try:
#             username = request.data['username']
#             password = request.data['password']
#             user = UserInfo.objects.filter(username=username, password=password).first()
#             if user is not None:
#                 payload = {
#                     'user': user.username,
#                     'token': user.token
#                 }
#                 token = create_token(payload)
#         except:
#             pass
#         result = {"token":token}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})

# class jwtOrder(APIView):
#     def post(self,request,format=None):
#         res   = 'None'
#         try:
#             token = request.data['token']
#             res = parse_payload(token,user='yzh')
#         except:
#             pass
#         result = {"res":res}
#         return JsonResponse(result, json_dumps_params={'ensure_ascii':False})