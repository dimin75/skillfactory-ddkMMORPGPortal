from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', AdvList.as_view()),
    path('<int:pk>', AdvView.as_view()),
    path('add', AdvCreateView.as_view()),
    path('edit/<int:pk>', AdvUpdateView.as_view()),
    path('responses', ResponseList.as_view()),
    path('responses/accept/<int:pk>', ResponseAcceptView.as_view()),
    path('responses/delete/<int:pk>', ResponseDeleteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
