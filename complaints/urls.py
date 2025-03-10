from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_complaint, name='submit_complaint'),  # Keep the submit route
    path('list/', views.complaint_list, name='complaint_list'),      # Keep the list route
    path('login/', views.login_view, name='login'),                    # Renamed to match consistency
    path('register/', views.register_view, name='register'),           # Renamed to match consistency
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),              # Added logout route
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)