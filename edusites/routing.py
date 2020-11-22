from channels.routing import ProtocolTypeRouter
application = ProtocolTypeRouter({
    # empty for now
})

#
# from django.urls import re_path
# from . import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/chat/room/(?P<course_id>\d+)/$', consumers.ChatConsumer),
# ]
