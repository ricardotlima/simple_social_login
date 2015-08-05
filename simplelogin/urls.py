from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    
    url(r'^logus/', TemplateView.as_view(template_name="logus.html")),
    url(r'^admin/', include(admin.site.urls)),
  
    #social auth
    url('', include('social.apps.django_app.urls', namespace='social')),    
    #logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    
)

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Debug static and media fiels urls 

#if settings.DEBUG: 
    #urlpatterns = patterns('', 
    #                       #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), 
    #                       url(r'', include('django.contrib.staticfiles.urls')), 
    #                       ) + urlpatterns 
    #urlpatterns += staticfiles_urlpatterns()
    


