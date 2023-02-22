'''def collection_testing(a):
    a_list = [1, 2, 3, 4]
    a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
    a_set = {1, 'Two', -3, 4.0}
    a_dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}
    # list
    print('List: ', a_list, '\n',
          type(a_list), '\n',
          'First:', a_list[0], '; Last:', a_list[-1], '\n',
          a_list[:int(len(a_list)/2)])
    for i in a_list:
        print(i.__index__(), ')', i)
    for i in a_list:
        i = int(input('Type: '))
        if 1 <= i <= 4:
            print(a_list[i-1])
            break
        else:
            print('Invalid.')

    print('\n')
    # tuple
    print('Tuple: ', a_tuple, '\n',
          type(a_tuple), '\n',
          'First:', a_tuple[0], '; Last: ', a_tuple[-1], '\n',
          a_tuple[:int(len(a_tuple)/2)])
    print('\n')
    # set
    print('Set: ', a_set, '\n',
          type(a_set), '\n',
          'First:', list(a_set)[0], '; Last:', list(a_set)[-1], '\n',
          list(a_set)[:len(a_set)//2])
    print('\n')
    # dictionary
    print('Dictionary: ', a_dictionary, '\n',
          type(a_dictionary), '\n',
          "First: ", list(a_dictionary.keys())[0], ',', list(a_dictionary.values())[0], '\n',
          "Last: ", list(a_dictionary.keys())[-1], ',', list(a_dictionary.values())[-1], '\n',
          list(a_dictionary.items())[:len(a_dictionary)//2])
    # for (key, value) in a_dictionary.items():
        # print ('%r: %r' % (key, value))
    # print(a_dictionary[:int(len(a_dictionary)/2)]) # call first half
    '''

a_list = [1, 2, 3, 4]
a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
a_set = {1, 'Two', -3, 4.0}
a_dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}


def collection_testing(a):
    if type(a) == list or tuple:
        # list
        print('List: ', a, '\n',  # printing collection
              type(a), '\n',  # collection type
              'First:', a[0], '; Last:', a[-1], '\n',  # First & last of collection
              a_list[:int(len(a)/2)])  # First half of collection
        for i in a:  # getting specific item
            print(i.__index__(), ')', i)
        for i in a:
            i = int(input('Type: '))
            if 1 <= i <= 4:
                print(a_list[i-1])
                break
            else:
                print('Invalid.')
        print('\n')
    elif type(a) == set:
        print('Set: ', a_set, '\n',
              type(a_set), '\n',
              'First:', list(a_set)[0], '; Last:', list(a_set)[-1], '\n',
              list(a_set)[:len(a_set)//2])
        for i in a_set:
            print(i.__index__(), ')', i)
        for i in a_set:
            i = int(input('Type: '))
            if 1 <= i <= 4:
                print(a_set[i-1])
                break
            else:
                print('Invalid.')
        print('\n')
        '''# tuple
        print('Tuple: ', a_tuple, '\n',
              type(a_tuple), '\n',
              'First:', a_tuple[0], '; Last: ', a_tuple[-1], '\n',
              a_tuple[:int(len(a_tuple)/2)])
        print('\n')
        # dictionary
        print('Dictionary: ', a_dictionary, '\n',
              type(a_dictionary), '\n',
              "First: ", list(a_dictionary.keys())[0], ',', list(a_dictionary.values())[0], '\n',
              "Last: ", list(a_dictionary.keys())[-1], ',', list(a_dictionary.values())[-1], '\n',
              list(a_dictionary.items())[:len(a_dictionary)//2])'''


if __name__ == '__main__':
    collection_testing(a_list)
    collection_testing(a_tuple)
