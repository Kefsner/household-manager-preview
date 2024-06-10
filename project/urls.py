from django.urls import path, include

urlpatterns = [
    path('', include('base.urls')),
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/', include('categories.urls')),
    path('creditcards/', include('creditcards.urls')),
]
