from django.contrib import admin
from django.urls import path,include
from year_book import views
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',include('accounts.urls')),
   #  path('admin_panel',include('admin_panel.urls')),
    path('',views.home,name='home'),
    path('year_book/',include('year_book.urls')),
    path('accounts/',include('accounts.urls')),
]
