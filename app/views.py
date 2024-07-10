import uuid
from requests import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsOwnerOrReadOnly, IsAdminOrOwner
from app.models import *
from app.serializers import *
from rest_framework.views import *
from rest_framework.generics import *
from django.utils import timezone


class LoginUser(APIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        queryset = CustemUser.objects.all()
        return queryset.filter(username=self.request.user.username)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user.id)
        key = uuid.uuid4()
        # Obektlarni qaytarish
        queryset = self.get_queryset()
        return Response(queryset.data, print('succsesss'), status=status.HTTP_200_OK)

    # ///////////////////////////////TeacherViewAPi////////////

class CourseList(APIView):
    def post(self, request):
        direction_name = request.data.get('direction')

        try:
            if request.method == 'POST' and direction_name:
                # Berilgan yo'nalish nomi bo'yicha kurslarni izlash
                courses_with_direction = Course.objects.filter(direction__name=direction_name)

                if courses_with_direction.exists():
                    # Topilgan kurslar mavjud
                    # Ushbu kurslarni serializer yordamida JSON shaklida qaytarish
                    serializer = CourseSerializers(courses_with_direction, many=True)
                    return Response({'message': 'Topilgan kurslar', 'data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    # Berilgan yo'nalish bo'yicha kurslar topilmadi
                    return Response({'message': 'Topilmagan kurslar'}, status=status.HTTP_404_NOT_FOUND)
            else:
                # POST so'rovi kelmasa yoki yo'nalish nomi kiritilmagan bo'lsa
                return Response({'message': 'Yoʻnalish nomi kiritilishi shart'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Xatolik yuzaga keldi
            return Response({'message': 'Xatolik yuzaga keldi: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)



class TeList(ListAPIView):
    queryset = CustemUser.objects.filter(userStatus='Teacher')
    serializer_class = UserSerializers
    permission_classes = [AllowAny,]


class TeCreate(CreateAPIView):
    queryset = CustemUser.objects.filter(userStatus='Teacher')
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]



class TeUpdate(UpdateAPIView):
    queryset = CustemUser.objects.filter(userStatus='Teacher')
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly, IsAuthenticated]

class TeDelete(DestroyAPIView):
    queryset = CustemUser.objects.filter(userStatus='Teacher')
    serializer_class = UserSerializers
    permission_classes = [IsAdminOrOwner, IsAuthenticated]

    

# //////////////////Student View /////////////////
class StList(ListAPIView):
    queryset = CustemUser.objects.filter(userStatus='Student')
    serializer_class = UserSerializers
    permission_classes = [AllowAny]


class StCreate(CreateAPIView):
    queryset = CustemUser.objects.filter(userStatus='Student')
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]



class StUpdate(UpdateAPIView):
    queryset = CustemUser.objects.filter(userStatus='Student')
    serializer_class = UserSerializers

class Stdelete(DestroyAPIView):
    queryset = CustemUser.objects.filter(userStatus='Student')
    serializer_class = UserSerializers



#////////////////Direction/////////////////
class DirectionList(ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = [AllowAny]


class DirectionCreate(CreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = [IsAdminUser]

class DirectionDelete(DestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = [IsAdminUser]

class DirectionUpdate(UpdateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = [IsAdminUser]




# //////////////////TopicCategoryApi////////////////////////
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AllowAny]
    


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]



class CategoryUpdate(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]

class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]
# //////////Course Index  Api///////////////


class CourseList(ListAPIView):
    serializer_class = CourseSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        current_time = timezone.now()
        return Course.objects.filter(live_time__gt=current_time)


class CourseCreate(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAdminUser]



class CourseUpdate(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAdminUser]



class CourseDelete(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAdminUser]


# elon view classlari

class ElonList(ListAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializers

class ElonCrate(CreateAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializers
    permission_classes = [IsAdminUser]


class ElonUpdate(UpdateAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializers
    permission_classes = [IsAdminUser]


class ElonDelete(DestroyAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializers
    permission_classes = [IsAdminUser]






