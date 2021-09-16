from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls.static import static
from django.conf import settings

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),


    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('person_add/', views.person_add),
    path('person/', views.person),


    path('yoonhee/', views.yoonhee),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
