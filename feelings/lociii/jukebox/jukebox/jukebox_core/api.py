from django.core.paginator import Paginator, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Count, Min, Q
from django.contrib.sessions.models import Session
from django.utils import formats
import os, re, time
from signal import SIGABRT
from django.contrib.auth.models import User
from .models import Song, Artist, Album, Genre, Queue, Favourite, Player, History

class api_base:
    count = 30
    user_id = None
    search_term = None
    search_title = None
    search_artist_name = None
    search_artist_title = None
    filter_year = None
    filter_genre = None
    filter_artist_id = None
    filter_album_title = None
    order_by_field = None
    order_by_director = None
    order_by_fields = []
    order_by_directions = ['asc', 'desc']
    order_by_default = None

    def set_count(self, count):
        if count > 100:
            self.count = 100
        elif count > 0:
            self.count = count

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_search_term(self, term):
        options = self.parseSearchString(
            (
                'title',
                'artist',
                'album',
                'genre',
                'year',
            ),
            term
        )
        for key, value in options.items():
            if key == 'title':
                self.set_search_title(value)
            elif key == 'artist':
                self.set_search_artist_name(value)
            elif key == 'album':
                self.set_search_album_title(value)
            elif key == 'genre':
                try:
                    genre = Genre.objects.all().filter