# BooksCollector Tests

Этот проект содержит тесты для класса `BooksCollector`.

## Описание тестов

1. **test_add_new_book_add_two_books**: Проверяет добавление двух новых книг.
2. **test_add_new_book_invalid_name**: Проверяет, что книга с длинным названием или пустым названием не добавляется.
3. **test_add_new_book_duplicate**: Проверяет, что дубликаты книг не добавляются.
4. **test_set_book_genre**: Проверяет установку жанра книги.
5. **test_set_book_genre_invalid_genre**: Проверяет, что нельзя установить несуществующий жанр.
6. **test_get_books_with_specific_genre**: Проверяет получение списка книг с определённым жанром.
7. **test_get_books_for_children**: Проверяет получение списка книг, подходящих для детей.
8. **test_add_book_in_favorites**: Проверяет добавление книги в избранное.
9. **test_add_book_in_favorites_not_in_books_genre**: Проверяет, что нельзя добавить в избранное книгу, которой нет в словаре.
10. **test_delete_book_from_favorites**: Проверяет удаление книги из избранного.
11. **test_get_list_of_favorites_books**: Проверяет получение списка избранных книг.