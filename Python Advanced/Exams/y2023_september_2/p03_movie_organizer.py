def movie_organizer(*args):
    movies_by_genres = {}
    for (name, genre) in args:
        if genre not in movies_by_genres:
            movies_by_genres[genre] = []
        movies_by_genres[genre].append(name)

    sorted_movies = dict(sorted(movies_by_genres.items(), key=lambda d: (-len(d[1]), d[0])))

    for (genre, movies) in sorted_movies.items():
        new_movies = sorted(movies)
        sorted_movies[genre] = new_movies

    string_to_print = ""

    for (genre, movies) in sorted_movies.items():
        string_to_print += f"{genre} - {len(movies)}\n"
        for movie in movies:
            string_to_print += f"* {movie}\n"

    return string_to_print
