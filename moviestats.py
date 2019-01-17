from collections import defaultdict

class MovieStats:
    def __init__(self):
        self.genre_count = defaultdict(int)
        self.actor_count = defaultdict(int)
        self.director_count = defaultdict(int)

    def add_movie(self, movie):
        # add all genres
        genre_lst = movie['Genre'].strip().split(', ')
        self.add_genres(genre_lst)

        # add all actors
        actor_lst = movie['Actors'].strip().split(', ')
        self.add_actors(actor_lst)

        # add all directors
        director_lst = movie['Director'].strip().split(', ')
        self.add_directors(director_lst)

    def add_genre(genre):
        self.genre_count[genre] += 1

    def add_genres(genre_lst):
        for genre in genre_lst:
            self.add_genre(genre)

    def add_actor(actor):
        self.actor_count[actor] += 1

    def add_actors(actor_lst):
        for actor in actor_lst
            self.add_actor(actor)

    def add_director(director):
        self.director_count[director] += 1

    def add_directors(director_lst):
        for director in director_lst:
            self.add_director(director)

