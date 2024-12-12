import time
from ClassAdressBook import AddressBook

class ConsoleInterFace:
    def __init__(self):
        self.address_book = AddressBook()

    def menu(self):
        print("Выберите действие:")
        print("1. Запустить обработку файла")
        print("2. Выйти")

    def process(self):
        while True:
            self.menu()
            choice = input("Введите ваш выбор: ")
            if choice == "1":
                file_path = input("Введите путь к файлу с расширением (полный путь): ")
                start_time = time.perf_counter()
                self.address_book.clear()
                try:
                    if file_path.endswith(".csv"):
                        self.address_book.read_from_csv(file_path)
                    elif file_path.endswith(".xml"):
                        self.address_book.read_from_xml(file_path)
                    else:
                        print("Неверный формат ввода, попробуйте еще раз!")
                        continue
                except FileNotFoundError:
                    print("Ошибка: Файл не найден. Проверьте имя и путь к файлу и попробуйте снова.")
                    continue
                except Exception as e:
                    print(f"Произошла ошибка: {e}. Попробуйте снова.")
                    continue

                self.address_book.results()
                end_time = time.perf_counter()
                print(f"Время обработки файла: {end_time - start_time:.4f} секунд")
            elif choice == "2":
                break
            else:
                print("Вы выбрали неверный пункт меню, попробуйте еще раз!")
