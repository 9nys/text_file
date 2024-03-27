def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Кількість слів у файлі '{file_path}': {word_count}")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


file_path = input("Введіть шлях до текстового файлу: ")

count_words_in_file(file_path)
