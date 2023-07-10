from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTests(TestCase):
    def setUp(self):
        self.book_store = Bookstore(10)

    def test_correct_initializing_of_bookstore_object(self):
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_book_limit_with_invalid_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.book_store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_correct__len__method(self):
        self.book_store.availability_in_store_by_book_titles["Harry Potter"] = 2
        self.book_store.availability_in_store_by_book_titles["Lord of the Rings"] = 2
        result = sum(self.book_store.availability_in_store_by_book_titles.values())

        self.assertEqual(4, result)

    def test_receive_book_but_capacity_is_reached_raise_exception(self):
        self.book_store.availability_in_store_by_book_titles["Harry Potter"] = 10

        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("Lord of the Rings", 1)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_for_the_first_time(self):
        self.book_store.receive_book("Harry Potter", 5)

        self.assertEqual(5, self.book_store.availability_in_store_by_book_titles["Harry Potter"])

    def test_receive_book_for_the_second_time(self):
        self.book_store.receive_book("Harry Potter", 5)
        result = self.book_store.receive_book("Harry Potter", 5)

        self.assertEqual(10, self.book_store.availability_in_store_by_book_titles["Harry Potter"])
        self.assertEqual("10 copies of Harry Potter are available in the bookstore.", result)

    def test_sell_book_with_invalid_key_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Harry Potter", 10)

        self.assertEqual("Book Harry Potter doesn't exist!", str(ex.exception))

    def test_sell_book_with_invalid_input_not_enough_copies_raise_exception(self):
        self.book_store.availability_in_store_by_book_titles["Harry Potter"] = 5

        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Harry Potter", 10)

        self.assertEqual(f"Harry Potter has not enough copies to sell. Left: "
                         f"{self.book_store.availability_in_store_by_book_titles['Harry Potter']}", str(ex.exception))

    def test_sell_book_with_valid_parameters(self):
        self.book_store.availability_in_store_by_book_titles["Harry Potter"] = 5
        result = self.book_store.sell_book("Harry Potter", 5)

        self.assertEqual("Sold 5 copies of Harry Potter", result)
        self.assertEqual(5, self.book_store.total_sold_books)
        self.assertEqual(0, self.book_store.availability_in_store_by_book_titles["Harry Potter"])

    def test_correct__str__method(self):
        self.book_store.availability_in_store_by_book_titles["Harry Potter"] = 10
        self.book_store.sell_book("Harry Potter", 5)
        result = str(self.book_store)

        self.assertEqual("Total sold books: 5\nCurrent availability: 5\n - Harry Potter: 5 copies", result)


if __name__ == "__main__":
    main()