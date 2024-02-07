from typing import Union


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

    # Function to check if a movie's IMDB score is above 5.5


def check_rating(movie_or_movie_id: Union[str, int], more_than = 5.5):
    rating: Union[float, None] = None
    if type(movie_or_movie_id) == int:
        rating = movies[movie_or_movie_id]['imdb']
    else:
        rating = list(filter(lambda x: x['name'] == movie_or_movie_id, movies))[0]['imdb']

    return rating > more_than

def above_5_5_movies(movies):
    lst = []
    for i in range(0, len(movies)):
        if check_rating(i):
            lst.append(movies[i])
    return lst

def filter_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

def average_imdb_score_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb_score(category_movies)

# Example usage:
print(check_rating("Usual Suspects")) 
print(above_5_5_movies(movies)) 
print(filter_by_category(movies, 'Romance')) 
print(average_imdb_score(movies)) 
print(average_imdb_score_by_category(movies, 'Romance')) 
