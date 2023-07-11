from unittest import TestCase, main
from project.movie import Movie


class MovieTests(TestCase):
    def setUp(self):
        self.movie = Movie("Titanic", 1997, 9.5)

    def test_check_for_proper_initializing(self):
        self.assertEqual("Titanic", self.movie.name)
        self.assertEqual(1997, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_check_if_name_is_empty_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_check_year_if_it_is_before_1887_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1850

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_append_name_when_does_not_exist(self):
        first = "Pesho"
        second = "Gosho"

        self.movie.add_actor(first)
        self.movie.add_actor(second)

        self.assertEqual([first, second], self.movie.actors)

    def test_add_actor_returns_error_message_with_duplicated_name(self):
        name = "Pesho"
        self.movie.actors = [name]

        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_greater_than_with_another_movie_with_lower_or_higher_rating(self):
        another_movie_name = "The Matrix"
        another_movie = Movie(another_movie_name, 1999, 2)

        first_result = self.movie > another_movie
        second_result = self.movie < another_movie

        expected_result = f'"{self.movie.name}" is better than "{another_movie_name}"'

        self.assertEqual(expected_result, first_result)
        self.assertEqual(expected_result, second_result)

    def test_valid_representation_of_movie(self):
        actors = ["Pesho", "Gosho"]
        self.movie.actors = actors
        actual_result = repr(self.movie)
        expected_result = f"Name: Titanic\n" \
                          f"Year of Release: 1997\n" \
                          f"Rating: 9.50\n" \
                          f"Cast: {', '.join(actors)}"

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
    
    
# Variant 2
# from project.movie import Movie
# from unittest import TestCase, main
# 
# 
# class MovieTests(TestCase):
#     def setUp(self):
#         self.movie = Movie("Titanic", 1997, 8.5)
#         self.other_movie = Movie("Robocop", 1998, 8.0)
# 
#     def test_correct_initializing(self):
#         self.assertEqual("Titanic", self.movie.name)
#         self.assertEqual(1997, self.movie.year)
#         self.assertEqual(8.5, self.movie.rating)
#         self.assertEqual([], self.movie.actors)
# 
#     def test_correct_name_cannot_be_empty_string_raise_value_error(self):
#         with self.assertRaises(ValueError) as ve:
#             self.movie.name = ""
# 
#         self.assertEqual("Name cannot be an empty string!", str(ve.exception))
# 
#     def test_correct_year_cannot_be_before_1887_raise_value_error(self):
#         with self.assertRaises(ValueError) as ve:
#             self.movie.year = 1886
# 
#         self.assertEqual("Year is not valid!", str(ve.exception))
# 
#     def test_add_actor_which_is_not_already_added(self):
#         self.movie.add_actor("Maria")
#         self.movie.add_actor("Josep")
# 
#         self.assertEqual(["Maria", "Josep"], self.movie.actors)
# 
#     def test_add_actor_which_is_already_added(self):
#         self.movie.actors = ["Maria"]
#         result = self.movie.add_actor("Maria")
# 
#         self.assertEqual("Maria is already added in the list of actors!", result)
# 
#     def test_correct__gt__method_first_movie_has_better_rating(self):
#         result = self.movie > self.other_movie
# 
#         self.assertEqual('"Titanic" is better than "Robocop"', result)
# 
#     def test_correct__gt_method_second_movie_has_better_rating(self):
#         self.other_movie.rating = 10.0
#         result = self.movie > self.other_movie
# 
#         self.assertEqual('"Robocop" is better than "Titanic"', result)
# 
#     def test_correct__repr__method(self):
#         self.movie.add_actor("Maria")
#         self.movie.add_actor("Josep")
#         result = str(self.movie)
#         expected_result = f"Name: Titanic\nYear of Release: 1997\nRating: 8.50\nCast: Maria, Josep"
# 
#         self.assertEqual(result, expected_result)
# 
# 
# if __name__ == "__main__":
#     main()
