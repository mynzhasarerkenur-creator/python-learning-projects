# patients = [
#     {"name": "Ali", "temp": 36.6},
#     {"name": "Erkenur", "temp": 38.2},
#     {"name": "Aida", "temp": 37.4},
#     {"name": "Marat", "temp": 39.1}
# ]
# filtered_patients = filter(
#     lambda patient: patient['temp'] >= 37,
#     patients
# )
 
# for patient in filtered_patients:
#     print(patient)


movies = [
    {"title": "Interstellar", "rating": 9.5},
    {"title": "Avatar", "rating": 8.2},
    {"title": "The Dark Knight", "rating": 9.8},
    {"title": "Inception", "rating": 9.1},
    {"title": "Titanic", "rating": 7.9},
    {"title": "The Matrix", "rating": 9.3}
]

sort_movies = sorted(
    movies,
    key= lambda movie: movie['rating'],
    reverse=True
)

filtered_movies = list(filter(lambda movie: movie['rating'] >= 8.5, sort_movies))

for movie in filtered_movies:
    print(movie)