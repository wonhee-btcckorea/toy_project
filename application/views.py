# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from application.serializers import *
from rest_framework.mixins import *
from rest_framework.views import APIView

import redis

class mysql_user(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)                  # post로 들어온 데이터(request.data)를 직렬화
            if serializer.is_valid():                                       # 직렬화 데이터 유효성 검사
                serializer.save()            # D에 저장?
                return Response(serializer.data, status=status.HTTP_201_CREATED)    # 들어간 데이터를 반환, 201 메세지 응답
            return Response("ERROR", status=status.HTTP_404_NOT_FOUND)      # 데이터가 유효하지 않으면 404 메세지 응답


    def get(self, request, id=None):
        if request.method == 'GET':
            try:
                user = User.objects.get(id=id)                              # url로 받은 id 파라미터로 DB의 데이터 검색
                serializer = UserSerializer(user)                           # 받아온 데이터를 직렬화
                return Response(serializer.data, status.HTTP_200_OK)        # 직렬화한 데이터 반환
            except User.DoesNotExist:                                       # 일치하는 데이터가 없다면 예외처리

                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        if request.method == 'PUT':
            try:
                id = request.data.get('id')
                user = User.objects.get(id=id)                              # url로 받은 id 파라미터로 DB의 데이터 검색
                serializer = UserSerializer(user, data=request.data)        # 받아온 데이터를 직렬화
                if serializer.is_valid():                                   # 변경된 데이터 저장
                    serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)        # 직렬화한 데이터 반환
            except User.DoesNotExist:                                       # 일치하는 데이터가 없다면 예외처리
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=None):
        if request.method == 'DELETE':
            try:
                user = User.objects.get(id=id)                              # url로 받은 id 파라미터로 DB의 데이터 검색
                user.delete()                                               # 데이터 삭제
                return Response("SUCCESS", status=status.HTTP_200_OK)
            except User.DoesNotExist:                                       # 일치하는 데이터가 없다면 예외처리
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)


class redis_user(APIView):

    queryset = RedisUser.objects.all()
    serializer_class = RedisUserSerializer
    r = redis.Redis(
        host='localhost',
        port=6379
    )

    def post(self, request):
        if request.method == 'POST':
            red = self.r
            id = request.data.get('id')
            name = request.data.get('name')

            if red.get(id) is not None:
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

            red.set(id, name)
            return Response("SUCCESS", status=status.HTTP_200_OK)

    def get(self, request, id=None):
        if request.method == 'GET':
            red = self.r
            name = red.get(id)

            if name is None:
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

            return Response(name, status=status.HTTP_200_OK)

    def put(self, request):
        if request.method == 'PUT':
            red = self.r

            id = request.data.get('id')
            name = request.data.get('name')
            if red.get(id) is None:
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

            red.getset(id, name)
            user = {
                "id": id,
                "name": name
            }
            return Response(user, status.HTTP_200_OK)

    def delete(self, request, id):
        if request.method == 'DELETE':
            red = self.r

            if red.get(id) is None:
                return Response("ERROR", status=status.HTTP_404_NOT_FOUND)

            red.set(id, "data expired...", None, 1, False, True)
            return Response("SUCCESS", status=status.HTTP_200_OK)

