
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import UserSerializer
from client.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@csrf_exempt
def isAdmin(request):

    data = request.POST.copy()
    data = list(data.keys())
    print("hekko :", data[0])
    data = data[0]
    print(data)
    user = Token.objects.get(key=data)
    username = User.objects.get(id=user.user_id)
    if username.is_superuser:
        admin = True
        return JsonResponse({'admin': admin})
    else:
        admin = False
        return JsonResponse({'admin': admin})

    # def create(self, request):
    #     for i in request.POST:
    #         print("data : ", i)

    # def user_list(request):
    #     if request.method == 'GET':
    #         users = User.objects.all()
    #         serializer = UserSerializer(users, many=True)
    #         return JsonResponse(serializer.data, safe=False)
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = UserSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, safe=False, status=201)
    #         return JsonResponse(serializer.errors, status=400)
