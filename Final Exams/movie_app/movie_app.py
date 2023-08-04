from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        user = self.__find_username_by_name(username)

        if user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        user = self.__find_username_by_name(username)

        if not user:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_username_by_name(username)

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user = self.__find_username_by_name(username)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user = self.__find_username_by_name(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))

        if not self.movies_collection:
            result = "No movies found."
        else:
            result = '\n'.join([movie.details() for movie in sorted_movies])

        return result

    def __str__(self):
        if not self.users_collection:
            result = "All users: No users."
        else:
            result = f"All users: {', '.join(user.username for user in self.users_collection)}"

        if not self.movies_collection:
            result2 = "All movies: No movies."
        else:
            result2 = f"All movies: {', '.join(movie.title for movie in self.movies_collection)}"

        return f"{result}\n{result2}"

    def __find_username_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

        return None

    def __find_movie_by_title(self, movie_title):
        for movie in self.movies_collection:
            if movie.title == movie_title:
                return movie

        return None

# Variant 2
# from project.movie_specification.movie import Movie
# from project.user import User


# class MovieApp:
#     def __init__(self):
#         self.movies_collection = []
#         self.users_collection = []

#     def register_user(self, username, age):
#         user = self.__find_user_by_username(username)

#         if user:
#             raise Exception("User already exists!")

#         new_user = User(username, age)
#         self.users_collection.append(new_user)
#         return f"{username} registered successfully."

#     def upload_movie(self, username, movie: Movie):
#         user = self.__find_user_by_username(username)

#         if not user:
#             raise Exception("This user does not exist!")

#         if movie.owner.username != user.username:
#             raise Exception(f"{username} is not the owner of the movie {movie.title}!")

#         if movie in self.movies_collection:
#             raise Exception("Movie already added to the collection!")

#         user.movies_owned.append(movie)
#         self.movies_collection.append(movie)
#         return f"{username} successfully added {movie.title} movie."

#     def edit_movie(self, username, movie: Movie, **kwargs):
#         user = self.__find_user_by_username(username)

#         if movie.owner.username != user.username:
#             raise Exception(f"{username} is not the owner of the movie {movie.title}!")

#         if movie not in self.movies_collection:
#             raise Exception(f"The movie {movie.title} is not uploaded!")

#         for key, value in kwargs.items():
#             setattr(movie, key, value)

#         return f"{username} successfully edited {movie.title} movie."

#     def delete_movie(self, username, movie: Movie):
#         user = self.__find_user_by_username(username)

#         if movie.owner.username != user.username:
#             raise Exception(f"{username} is not the owner of the movie {movie.title}!")

#         if movie not in self.movies_collection:
#             raise Exception(f"The movie {movie.title} is not uploaded!")

#         self.movies_collection.remove(movie)
#         user.movies_owned.remove(movie)
#         return f"{username} successfully deleted {movie.title} movie."

#     def like_movie(self, username, movie: Movie):
#         user = self.__find_user_by_username(username)

#         if movie.owner.username == user.username:
#             raise Exception(f"{username} is the owner of the movie {movie.title}!")

#         if movie in user.movies_liked:
#             raise Exception(f"{username} already liked the movie {movie.title}!")

#         movie.likes += 1
#         user.movies_liked.append(movie)
#         return f"{username} liked {movie.title} movie."

#     def dislike_movie(self, username, movie: Movie):
#         user = self.__find_user_by_username(username)

#         if movie not in user.movies_liked:
#             raise Exception(f"{username} has not liked the movie {movie.title}!")

#         movie.likes -= 1
#         user.movies_liked.remove(movie)
#         return f"{username} disliked {movie.title} movie."

#     def display_movies(self):
#         ordered_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))

#         if not ordered_movies:
#             return "No movies found."
#         return "\n".join([movie.details() for movie in ordered_movies])

#     def __str__(self):
#         if not self.users_collection:
#             result = "All users: No users."
#         else:
#             result = f"All users: {', '.join(user.username for user in self.users_collection)}"

#         if not self.movies_collection:
#             result2 = "All movies: No movies."
#         else:
#             result2 = f"All movies: {', '.join(movie.title for movie in self.movies_collection)}"

#         return f"{result}\n{result2}"

#     def __find_user_by_username(self, username):
#         for user in self.users_collection:
#             if user.username == username:
#                 return user

#         return None
