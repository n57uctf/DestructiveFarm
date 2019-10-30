import re
import urllib.request


def match_flag(text: str, regexp: str) -> list:
    """
    Возвращает все результаты поиска в text регулярного выражения regexp

    :param text
    :param regexp
    :return: список (может быть пустым) совпадающих строк
    """
    return re.findall(regexp, text)


def download_file(url: str, path: str):
    """
    Скачивает файл

    :param url: путь до файла (https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
    :param path: название загружаемого файла (image.img)
    """
    urllib.request.urlretrieve(url, path)
