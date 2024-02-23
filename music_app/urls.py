from django.contrib import admin
from django.urls import path, include, re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('likesong', views.likesong, name = "likesong"),
    path('allSongs', views.allSongs, name="allSongs"),

    # path('allBooks/fiction', views.fiction, name="fiction"),
    # path('allBooks/thriller', views.thriller, name="thriller"),
    # path('allBooks/casual', views.casual, name="casual"),
    # path('allBooks/romance', views.romance, name="romance"),

    path('allBooks/<str:genre>/', views.genre_books, name='genre_books'),

    path('history', views.history, name="history"),
    path('song/<int:id>', views.songpost, name='songpost'),
    path('album/<int:id>', views.singerpost, name='singerpost'),
    path('createPlaylist', views.createPlaylist, name='createPlaylist'),
    path('myPlaylist/<int:id>', views.myPlaylist, name='myPlaylist'),
    path('addSongToPlaylist', views.addSongToPlaylist, name='addSongToPlaylist'),
    path('deletePlaylist', views.deletePlaylist, name='deletePlaylist'),
    path('searchResults', views.searchResults, name='searchResults'),
    path('allBooks', views.allBooks, name="allBooks"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    
    path('accounts/', include('allauth.urls')),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
