from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class UserListView(APIView):
    authentication_classes = []
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            response_data = {
                'user': {
                    'id': user.id,
                    'email': user.email,
                    "token": access_token,
                    "refresh_token": refresh_token
                }
            }

            return Response(response_data)
        return Response(serializer.errors)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            return Response({
                "email": user.email,
                "token": access_token,
                "refresh_token": refresh_token
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
