def collection_testing():
    a_list = [1, 2, 3, 4]
    a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
    a_dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}
    first_half = int(len(a_list)/2)
    print('List: ', a_list)
    print(type(a_list))
    print(a_list[0], ',', a_list[-1])
    print(a_list[:int(len(a_list)/2)])
    print('\n')
    print('Tuple: ', a_tuple)
    print(type(a_tuple))
    print(a_tuple[0], ',', a_tuple[-1])
    print(a_tuple[:int(len(a_tuple)/2)])
    print('\n')
    print('Dictionary: ', a_dictionary)
    print(type(a_dictionary))
    print(list(a_dictionary.keys())[0], ',', list(a_dictionary.values())[0])
    print(list(a_dictionary.keys())[-1], ',', list(a_dictionary.values())[-1])
    # print(a_dictionary[:int(len(a_dictionary)/2)]) # call first half


if __name__ == '__main__':
    collection_testing()

