from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('api.account.urls_auth')),
    path('users/', include('api.account.urls')),

    path('categories/', include('api.titles.urls.category')),
    path('titles/', include('api.titles.urls.titles')),
    path('genres/', include('api.titles.urls.genre')),
]
