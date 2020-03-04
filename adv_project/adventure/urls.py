from django.conf.urls import url
from . import api


"""
commented out for now because api has not yet been implemented, but this is how it should look when api
gets implemented and what the methods will be

"""

from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),

    url('get_rooms', api.getRoom),
]
