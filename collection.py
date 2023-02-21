def collection_testing():
    a_list = [1, 2, 3, 4]
    a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
    a_set = {1, 'Two', -3, 4.0}
    a_dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}
    print('List: ', a_list, '\n',
          type(a_list), '\n',
          'First:', a_list[0], '; Last:', a_list[-1], '\n',
          a_list[:int(len(a_list)/2)])
    print('\n')
    print('Tuple: ', a_tuple, '\n',
          type(a_tuple), '\n',
          'First:', a_tuple[0], '; Last: ', a_tuple[-1], '\n',
          a_tuple[:int(len(a_tuple)/2)])
    print('\n')
    print('Set: ', a_set, '\n',
          type(a_set), '\n',
          'First:', list(a_set)[0], '; Last:', list(a_set)[-1], '\n',
          list(a_set)[:len(a_set)//2])
    print('\n')
    print('Dictionary: ', a_dictionary, '\n',
          type(a_dictionary), '\n',
          "First: ", list(a_dictionary.keys())[0], ',', list(a_dictionary.values())[0], '\n',
          "Last: ", list(a_dictionary.keys())[-1], ',', list(a_dictionary.values())[-1], '\n',
          list(a_dictionary.items())[:len(a_dictionary)//2])
    # for (key, value) in a_dictionary.items():
        # print ('%r: %r' % (key, value))
    # print(a_dictionary[:int(len(a_dictionary)/2)]) # call first half


if __name__ == '__main__':
    collection_testing()
