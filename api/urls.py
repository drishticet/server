from django.urls import include, path
from .views import LeaderBoard, UsernameListView

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('user.urls')),
    path('leaderboard/', LeaderBoard.as_view()),
    path('usernamelist/', UsernameListView.as_view()),
]
