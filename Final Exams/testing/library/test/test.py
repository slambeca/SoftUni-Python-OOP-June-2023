from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self):
        self.library = Library("Rusenska biblioteka")

    def test_correct_initializing(self):
        self.assertEqual("Rusenska biblioteka", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_if_name_is_an_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_reader_method_unsuccessful(self):
        self.library.add_reader("John")
        result = self.library.add_reader("John")

        self.assertEqual("John is already registered in the Rusenska biblioteka library.", result)

    def test_add_reader_method_successful(self):
        self.library.add_reader("John")
        self.library.add_reader("Magda")

        self.assertEqual({"John": [], "Magda": []}, self.library.readers)

    def test_add_book_unsuccessful_because_it_is_already_there(self):
        self.library.add_book("Henri Charriere", "Papillon")
        self.library.add_book("Henri Charriere", "Papillon")

        self.assertEqual({"Henri Charriere": ["Papillon"]}, self.library.books_by_authors)

    def test_add_book_successful_variant_one(self):
        self.library.add_book("Henri Charriere", "Papillon")

        self.assertEqual({"Henri Charriere": ["Papillon"]}, self.library.books_by_authors)

    def test_add_book_successful_variant_two(self):
        self.library.books_by_authors["Henri Charriere"] = ["Papillon"]
        self.library.add_book("Henri Charriere", "Moleste")

        self.assertEqual({"Henri Charriere": ["Papillon", "Moleste"]}, self.library.books_by_authors)

    def test_rent_book_unsuccessful_reader_does_not_exist(self):
        result = self.library.rent_book("Neno", "Henri Charriere", "Papillon")

        self.assertEqual("Neno is not registered in the Rusenska biblioteka Library.", result)

    def test_rent_book_unsuccessful_author_does_not_exist(self):
        self.library.add_reader("Neno")
        result = self.library.rent_book("Neno", "Henri Charriere", "Papillon")

        self.assertEqual("Rusenska biblioteka Library does not have any Henri Charriere's books.", result)

    def test_rent_book_unsuccessful_book_does_not_exist(self):
        self.library.add_reader("Neno")
        self.library.add_book("Henri Charriere", "Papillon")
        result = self.library.rent_book("Neno", "Henri Charriere", "Moleste")

        self.assertEqual("""Rusenska biblioteka Library does not have Henri Charriere's "Moleste".""", result)

    def test_rent_book_successful(self):
        self.library.add_reader("Neno")
        self.library.add_book("Henri Charriere", "Papillon")
        self.library.add_book("Henri Charriere", "Moleste")

        self.library.rent_book("Neno", "Henri Charriere", "Papillon")

        self.assertEqual({"Henri Charriere": ["Moleste"]}, self.library.books_by_authors)
        self.assertEqual({'Neno': [{'Henri Charriere': 'Papillon'}]}, self.library.readers)


if __name__ == "__main__":
    main()