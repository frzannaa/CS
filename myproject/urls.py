from django.urls import path, include
from django.contrib import admin
from myapp import views as myappViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Custom URL patterns for your app
    path('', myappViews.home, name='home'),
    path('about/', myappViews.about, name='about'),  # Including the 'about' view function here
    path('signup/', myappViews.signup, name='signup'),

    # Include URL patterns from myapp.urls
    path('myapp/', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),

]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
