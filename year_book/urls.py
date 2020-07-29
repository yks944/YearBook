from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.updateprofile,name='update_profile'),
    path('achv_options/',views.options,name='achv_options'),
    path('achv/<str:cate>/',views.category,name='category'),
    path('achv_list/<str:cate>',views.achv_list,name='achv_list'),
    path('achv_detailed/<str:utype>/<str:username>/',views.getdetails,name = 'achv_detailed'),
    path('t_achv/',views.t_achv,name='t_achv'),
    path('s_achv',views.s_achv,name='s_achv'),
    path('admin_t_achv<str:cate>/',views.category2,name='admin_t_achv'),
    path('admin_s_achv<str:cate>/',views.category3,name='admin_s_achv'),
    path('admin_achv_list/<str:cate>',views.achv_list2,name='admin_achv_list'),
    path('admin_achv_detailed/<str:utype>/<str:username>/',views.getdetails2,name = 'admin_achv_detailed'),
    path('add_s_achv/',views.add_s_achv,name = 'add_s_achv'),
    path('add_t_achv/',views.add_t_achv,name = 'add_t_achv'),
]