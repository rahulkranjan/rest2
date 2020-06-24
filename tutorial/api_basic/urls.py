
from django.urls import path,include
from .views import ArticleAPIView, ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import GeneratePdf

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
 
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('pdf/', GeneratePdf.as_view()),

 
 
]