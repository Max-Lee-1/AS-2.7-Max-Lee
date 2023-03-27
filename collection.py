# this is not the assessment -
# to see AS 2.7, please go to AS_2.7_Headphone_Recommendation.py








import array as arr

a_list = [1, 2, 3, "4"]
a_array = arr.array("b", [1, 2, 3, 4])
a_tuple = (1, [2.0, 2.1, 2.2], 3, 4.0)
a_set = {1, 'Two', -3, 4.0}
a_dictionary = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}


def collection_testing(a):
    print(a, '\n',
          type(a), '\n',
          'First item:', next(iter(a)), '; Last item:', list(a)[-1], '\n',  # First & last of collection
          'First half of list:', list(a)[:len(a)//2])  # First half of collection
    i = 0
    while i < 5:
        for i, item in enumerate(a):  # getting specific item and its index
            i += 1
            print(i, ') ', item)
        while True:  # Loop until a valid input is received
            try:
                i = int(input('Please select item you want: '))
                if 1 <= i <= len(a):
                    print('Result:', list(a)[i-1])
                    i = 5
                    print('\n')
                    break
                else:
                    print('Invalid, please type the according no. given.')
            except ValueError:
                print('Invalid input. Please type an integer')


if __name__ == '__main__':
    collection_testing(a_list)
    collection_testing(a_array)
    collection_testing(a_tuple)
    collection_testing(a_set)
    collection_testing(a_dictionary)

    '''if type(a) == list or type(a) == tuple: 
        
        print('\n')
    elif type(a) == set:
        print('Set: ', a, '\n',
              type(a), '\n',
              'First:', next(iter(a)), '; Last:', list(a)[-1], '\n',  # First & last of collection
              list(a)[:len(a)//2])  # First half of collection
        for i, item in enumerate(a):  # getting specific item and its index
            print(i + 1, ')', item)
        while True:  # Loop until a valid input is received
            try:
                i = int(input('Type: '))
                if 1 <= i <= len(a):
                    print(list(a)[i-1])
                    break
                else:
                    print('Invalid.')
            except ValueError:
                print('Invalid input.')
        print('\n')
    elif type(a) == dict:
        print('Dictionary: ', a, '\n',
              type(a), '\n',
              'First:', next(iter(a)), '; Last:', list(a)[-1], '\n',  # First & last of collection
              list(a)[:len(a)//2])  # First half of collection
        for i, item in enumerate(a):  # getting specific item and its index
            print(i + 1, ')', item)
        while True:  # Loop until a valid input is received
            try:
                i = int(input('Type: '))
                if 1 <= i <= len(a):
                    print(list(a)[i-1])
                    break
                else:
                    print('Invalid.')
            except ValueError:
                print('Invalid input.')
        print('\n')
    else:
        print('Unsupported collection type.')  # Inform the user that the collection type is not supported
        
        
        # tuple
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
              list(a_dictionary.items())[:len(a_dictionary)//2])
        
        
    def collection_testing(a):
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
