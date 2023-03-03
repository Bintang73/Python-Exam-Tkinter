import urllib.request,json,requests

def get_movies_list():
    url = "https://api.themoviedb.org/3/discover/movie?api_key=d304673657c45d10261cad6e3f07aeb8"
    url2 = "https://api.themoviedb.org/3/genre/movie/list?api_key=d304673657c45d10261cad6e3f07aeb8&language=en-US"

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    response2 = urllib.request.urlopen(url2)
    movies2 = response2.read()
    dict2 = json.loads(movies2)

    movies = []

    for movie in dict["results"]:
        acc = []
        for genreid in movie["genre_ids"]:
            for moviez in dict2["genres"]:
                if genreid == moviez["id"]:
                    acc.append(moviez["name"])

        movie = {
            "title": movie["title"],
            "genre": acc
            
        }
        movies.append(movie)

    popular = movies[0:3] 
    return popular


abc = get_movies_list()
print(abc)