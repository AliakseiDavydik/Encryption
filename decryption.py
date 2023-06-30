import pyAesCrypt
import os


# функция дешифровки файла
def decryption(file, password):
    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("Файл [" + str(os.path.splitext(file)[0]) + "] расшифрован")

    # удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def go_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            # если находим директорию, то повторяем цикл
            go_dirs(path, password)


password = input("Введите пароль для расшифровки: ")
go_dirs("C:/Users/37529/PycharmProjects/Encryption/file", password)
