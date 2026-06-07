import json


class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def show_movies(self):
        print(f"название: {self.title}")
        print(f"жанр: {self.genre}")
        print(f"Оценка: {self.rating}")

    def to_dict(self):
        return {"title": self.title, "genre": self.genre, "rating": self.rating}


movies = []

try:
    with open("movie/movie.json", "r") as files:
        movies_data = json.load(files)
        for data in movies_data:
            movies.append(Movie(data["title"], data["genre"], data["rating"]))
except (FileNotFoundError, json.JSONDecodeError):
    movies_data = []

while True:
    print(
        '1 добавить\n'
        '2 показать\n'
        '3 найти по названию\n'
        '4 выйти\n'     
        )
    choise = input('выбрать: ')

    if choise == '1':
        title = input('название: ')
        genre = input('жанр: ')
        rating = input('рейтинг: ')
        movies.append(Movie(title,genre,rating))
        print('фильм добавленo')
    elif choise =='2':
        if not movies:
            print('No movies')
        for num, movie in enumerate(movies, start = 1):
            print(f'{num}.', end = '')
            movie.show_movies()
            print()
    elif choise == '3':
        search = input('введите название фильма: ')
        print()
        found = False
        for movie in movies:
            if search in movie.title:
                movie.show_movies()
                print()
                found = True
        if found ==False:
            print('Movie is not found ')

    elif choise =='4':
        movies_data = []
        for movie in movies:
            movies_data.append(movie.to_dict())
        with open("movie/movie.json", 'w') as files:
            json.dump(movies_data, files, indent=4)
        break
