from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView

class UserListView(APIView):
    authentication_classes = []
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print("Serializer Created", serializer.is_valid(raise_exception=True))
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'user': {
                    'id': user.id,
                    'email': user.email,
                }
            }

            return Response(response_data)
        return Response(serializer.errors)
