from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about_us,name='about'),
    path('contact/',views.contact,name='contact'),
    path('shop/product/<slug:slug>/', views.product_details,name='product_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)