from django.contrib import admin
from django.urls import path, include


admin.site.site_header ="Ice creams bale Admin"
admin.site.site_title ="Ice creams bale Admin portal"
admin.site.index_title ="Welcom to Ice creams bale"




urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('blog.urls')),
    


]
