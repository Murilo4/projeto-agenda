from django.urls import path, include
from contact import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path("", views.index, name='index'),

    #contact (CRUD)
        path('contact/<int:contact_id>/', views.contact, name='contact'),
        path('contact/create/', views.create, name='contact'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
