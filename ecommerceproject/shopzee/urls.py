
from django.urls import path,include
from . import views
app_name='shopzee'

urlpatterns = [

    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodcatdetail'),


]