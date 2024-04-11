from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
            raise Exception("User already exists!")
        except StopIteration:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = None
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:  # Judge does not accept comparison between two objects, we have to do it through usernames
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        try:
            other_movie = next(filter(lambda m: m == movie, self.movies_collection))
            raise Exception("Movie already added to the collection!")
        except StopIteration:
            user.movies_owned.append(movie)
            self.movies_collection.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        try:
            edit_movie = next(filter(lambda m: m == movie, self.movies_collection))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for (edit, new_value) in kwargs.items():
            setattr(movie, edit, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        try:
            edit_movie = next(filter(lambda m: m == movie, self.movies_collection))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = list(sorted(self.movies_collection, key=lambda m: (-m.year, m.title)))
        return "\n".join(x.details() for x in sorted_movies)

    def __str__(self):
        users = "No users." if not self.users_collection else ', '.join(x.username for x in self.users_collection)
        movies = "No movies." if not self.movies_collection else ', '.join(x.title for x in self.movies_collection)

        return f"All users: {users}\nAll movies: {movies}"
