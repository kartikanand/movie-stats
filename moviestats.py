from collections import defaultdict

def get_max_count_items(count_dict):
    """
        get items with highest count
        this function returns a list
        since there can be more than
        one item with the same highest
        count
    """

    curr_max_count = float('-inf')
    curr_max_items = []

    for k, v in count_dict.items():
        if v > curr_max_count:
            curr_max_items = [k]
            curr_max_count = v
        elif v == curr_max_count:
            curr_max_items.append(k)

    return curr_max_items

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

    def add_genre(self, genre):
        self.genre_count[genre] += 1

    def add_genres(self, genre_lst):
        for genre in genre_lst:
            self.add_genre(genre)

    def add_actor(self, actor):
        self.actor_count[actor] += 1

    def add_actors(self, actor_lst):
        for actor in actor_lst:
            self.add_actor(actor)

    def add_director(self, director):
        self.director_count[director] += 1

    def add_directors(self, director_lst):
        for director in director_lst:
            self.add_director(director)

    def get_max_count_genres(self):
        return get_max_count_items(self.genre_count)

    def get_max_count_actors(self):
        return get_max_count_items(self.actor_count)

    def get_max_count_directors(self):
        return get_max_count_items(self.director_count)

    def print_stats(self):
        # get genres with highest count
        print('Most loved genres')
        print(self.get_max_count_genres())

        # get actors with highest count
        print('Most loved actors')
        print(self.get_max_count_actors())

        # get directors with highest count
        print('Most loved directors')
        print(self.get_max_count_directors())

