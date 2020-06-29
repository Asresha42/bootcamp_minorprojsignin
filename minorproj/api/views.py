from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import UsersAPI
from .serializers import UsersAPI


class UserApiView(APIView):
    def get(self, request):
        # print(request.data)
        queryset = UsersAPI.objects.filter(email=request.data.get('email')).values().first()
        if queryset:
            return Response('Congo')
        else:
            return Response("Invalid")
    def post(self, request):
        pass

