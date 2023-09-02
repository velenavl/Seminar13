# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений

def get_dict(my_dict, key, value = 20):
    try:

        res = my_dict[key]
    except KeyError as e:
        print("такой ключа нет в словаре")
        res = value
    return res


if __name__ == '__main__':
    my_dict = {'g' : 1, 'j' : 2}
    print(get_dict(my_dict, 'gg', 30 ))
    