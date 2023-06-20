from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('loginasuser/',views.loginasuser,name='loginasuser'),
    path('loginastutor/',views.loginastutor,name='loginastutor'),
    path('signupasuser/',views.signupasuser,name='signupasuser'),
    path('signupastutor/',views.signupastutor,name='signupastutor'),
    path('userpage/',views.userpage,name='userpage'),
    path('userpage1/',views.userpage1,name='userpage1'),
    path('afterlogin/',views.afterlogin,name='afterlogin'),
    path('languages/',views.languages,name='languages'),
    path('teachers/',views.teachers,name='teachers'),
    path('choiceofteacher/',views.choiceofteacher,name='choiceofteacher'),
    path('profilepage/',views.profilepage,name='profilepage'),
    path('teacherlogin/',views.teacherlogin,name='teacherlogin'),
    path('teacherprofile/',views.teacherprofile,name='teacherprofile'),
    path('teacherstudent/',views.teacherstudent,name='teacherstudent'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('scheduleclass/',views.scheduleclass,name='scheduleclass'),
    path('joincall/',views.joincall,name='joincall'),
    path('call/',views.call,name='call'),
    path('logout/',views.logout, name='logout'),
    path('payment/',views.payment,name='payment')
]


