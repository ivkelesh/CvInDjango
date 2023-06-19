from django.urls import path, include
from cv.views import CvView


urlpatterns = [
    path('', CvView.as_view(), name='cv'),
    path('<int:id>', CvView.as_view(), name='cv'),
]
