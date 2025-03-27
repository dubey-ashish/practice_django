from rest_framework import routers
from django.contrib import admin
from .views import BookViewSet,AuthorViewSet
from django.urls import path,include


router=routers.DefaultRouter()  #DefaultRouter() is an object

router.register(r'books', BookViewSet)
# r before strings ensures \(backslash) are treated literally
# so that it doesn't start creating new lines etc.
# No need here but it's used in cases like Windows File Paths
router.register(r'authors', AuthorViewSet)


# The empty string '' means it’s included at the root (/).
# Then all the urls that you registered with the router just before is included in the path after that
# It's a way to group and structure your API endpoints neatly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

