from django.templatetags.static import static
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views import *
from djangoProject import settings



urlpatterns = [
    
    # ///////////////////Teacher Path///////////////////////////////
    path("TeacherList/", TeList.as_view(), name="TeacherList"),
    path("TeacherCreate/", TeCreate.as_view(), name="TeacherCreate"),
    path("TeacherDelete/<int:pk>/", TeDelete.as_view(), name="TeacherDelete"),
    path("TeacherUpdate/<int:pk>/", TeUpdate.as_view(), name="TeacherUpdate"),

    # /////////////Student Path ////////////////////////////////////////
    path("StudentList/",StList.as_view(), name="Stlist"),
    path("StudentCreate/", StCreate.as_view(), name="StCreate"),
    path("StudentUpdate/<int:pk>/", StUpdate.as_view(), name="StUpdate"),
    path("StudentDelete/<int:pk>/", Stdelete.as_view(), name="StDelete"),


    #/////Direction ///////
    path("Direction/", DirectionList.as_view(), name="direction"),
    path("DirCreate/", DirectionCreate.as_view(), name="DirectionCreate"),
    path("DirUpdate/<int:pk>/", DirectionUpdate.as_view(), name="DiectionUpdaate"),
    path("DirDelete/<int:pk>/", DirectionDelete.as_view(), name="DirectionDelete"),


    #/////Category Path //////////
    path("Category/", CategoryList.as_view(), name="category"),
    path("CategoryCreate/", CategoryCreate.as_view(), name="CategoryCreate"),
    path("CategoryUpdate/<int:pk>/", CategoryUpdate.as_view(), name="CategoryUpdate"),
    path("CategoryDel/<int:pk>/", CategoryDelete.as_view(), name="Categorydel"),

    path("Course/", CourseList.as_view(), name="course"),
    path("CourseCreate/", CourseCreate.as_view(), name="coursecreate"),
    path("CourseUpdate/<int:pk>/", CourseUpdate.as_view(), name="courseupdate"),
    path("CourseDel/<int:pk>/", CourseDelete.as_view(), name="coursedel"),

    #Elon Url lari
    path("Elonlar/",ElonList.as_view(), name='elon'),
    path("ElonCreate/", ElonCrate.as_view(), name="eloncreate"),
    path("ElonUpdate/<int:pk>/", ElonUpdate.as_view(), name="update"),
    path("Elondelete/<int:pk>/", ElonDelete.as_view(), name="elonDelete"),




    #//////////all apis////////////////////////
    path("CourseListApi/", CourseList.as_view(), name="courselistapi"), 


    #///////////////// authenticated ////////////////////////////////////


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LoginUser.as_view(), name='login')
    #
    # path('auth-drf/', include('rest_framework.urls')),  # new
    # re_path(r'^auth/', include('djoser.urls')),  # new
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




