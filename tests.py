import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ["A" * 41, ""])
    def test_add_new_book_invalid_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 1")
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self, collector):
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Фантастика")
        assert collector.get_book_genre("Book 1") == "Фантастика"

    @pytest.mark.parametrize("genre", ["Invalid Genre", ""])
    def test_set_book_genre_invalid_genre(self, collector, genre):
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", genre)
        assert collector.get_book_genre("Book 1") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 1", "Фантастика")
        collector.set_book_genre("Book 2", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Book 1"]

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 1", "Фантастика")
        collector.set_book_genre("Book 2", "Ужасы")
        assert collector.get_books_for_children() == ["Book 1"]

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        assert "Book 1" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books_genre(self, collector):
        collector.add_book_in_favorites("Book 1")
        assert "Book 1" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 1")
        assert "Book 1" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_book_in_favorites("Book 1")
        collector.add_book_in_favorites("Book 2")
        assert collector.get_list_of_favorites_books() == ["Book 1", "Book 2"]