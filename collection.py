def collection_testing():
    a_list = [1, 2, 3, 4]
    a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
    a_dictionary = {'One': 1, 'Two': 2, 'Three': 3}
    print(a_list)
    print(type(a_list))
    print(a_list[0])
    print(a_tuple)
    print(type(a_tuple))
    print(a_tuple[0])
    print(a_dictionary)
    print(type(a_dictionary))
    print(list(a_dictionary.keys())[0], list(a_dictionary.values())[0])


if __name__ == '__main__':
    collection_testing()

