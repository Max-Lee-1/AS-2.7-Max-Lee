''' Headphone/Earbuds recommendation program
    users have to fill in requirements to narrow result
    Two categories of True Wireless(TW): TW Headphones & TW Earbuds (use collections)
    Each category has 10-20 in collections, total less than 40
    Requirements (variables): Price range: $1 - $2000
                              Brand: [insert selection chart]
                              Functions: E.g. Noise Cancelling, Ambient sound...
                              Support Codec: E.g. AAC, SBC, LDAC...
                              App support: Y/N / Both
                              Battery Life: [Selection time range]
                              Speciality (added form reference): the best overall, Best in audio, best in user-friendly...
                              Info: Ship Y/N; Retail Y/N; Overall rating (May add other ratings);
'''

import sys
# dictionary for options - includes price, brand, functions, Bluetooth Codec, App support, Battery Life and Speciality
# need to add the options one by one
# Pricing on 22 Mar 2023
# headphone: wireless, over-ear
headphone_dict = {
    'Anker SoundCore Life Q30': {'brand': 'Anker',
                                 'price': 159.99,
                                 'functions': 'Active Noise Cancelling, Voice Assistant, Passive Noise Cancelling',
                                 'codecs': 'SBC, AAC',
                                 'app support': 'No',
                                 'battery life': 60},
    'Apple Airpods Max': {'brand': 'Apple',
                          'price': 999.00,
                          'functions': 'Active Noise Cancelling, Ambient Sound',
                          'codecs': 'AAC',
                          'app support': 'No',
                          'battery life': 20},
    'Belkin Soundform Mini': {'brand': 'Belkin',
                              'price': 99.99,
                              'functions': 'Wireless, Voice Assistant',
                              'codecs': 'SBC, AAC',
                              'app support': 'Yes',
                              'battery life': 30},
    'Bose Noise Cancelling Headphones 700': {'brand': 'Bose',
                                             'price': 599.95,
                                             'functions': 'Active Noise Cancelling, Voice Assistant',
                                             'codecs': 'SBC, AAC',
                                             'app support': 'Yes',
                                             'battery life': 20},
    'Bowers & Wilkins Px7 S2 Headphones': {'brand': 'Bowers & Wilkins',
                                           'price': 899.00,
                                           'functions': 'Active Noise Cancelling, Ambient Sound',
                                           'codecs': 'aptX Adaptive, aptX HD, aptX, AAC, SBC',
                                           'app support': 'Yes',
                                           'battery life': 30},
    'Edifier W860NB': {'brand': 'Edifier',
                       'price': 189.95,
                       'functions': 'Active Noise Cancelling, Voice Assistant, Passive Noise Cancelling',
                       'codecs': 'SBC, AAC, aptX',
                       'app support': 'Yes',
                       'battery life': 35},
    'Logitech G435 LIGHTSPEED Wireless': {'brand': 'Logitech',
                                          'price': 249.90,
                                          'functions': 'Gaming',
                                          'speciality': 'best for gaming',
                                          'codecs': 'SBC, AAC',
                                          'app support': 'No',
                                          'battery life': 18},
    'Sennheiser Momentum 4 Wireless': {'brand': 'Sennheiser',
                                       'price': 679.95,
                                       'functions': 'Active Noise Cancelling, Ambient Sound, Voice Assistant',
                                       'codecs': 'SBC, AAC, aptX, aptX Low Latency, LHDC',
                                       'app support': 'Yes',
                                       'battery life': 60},
    'Sony WH-1000XM4': {'brand': 'Sony',
                        'price': 414.00,
                        'functions': 'Active Noise Cancelling, Ambient Sound, Voice Assistant',
                        'codecs': 'LDAC, SBC, AAC',
                        'app support': 'Yes',
                        'battery life': 30},
    'Sony WH-1000XM5': {'brand': 'Sony',
                        'price': 537.99,
                        'functions': 'Active Noise Cancelling, Ambient Sound, Voice Assistant',
                        'codecs': 'LDAC, SBC, AAC',
                        'app support': 'Yes',
                        'battery life': 30},
}

# earbuds: wireless buds, in-ear
earbud_dict = {
    'Apple Airpods Pro (Gen 2)': {'brand': 'Apple',
                                  'price': 379.00,
                                  'functions': 'Bluetooth 5.0, Wireless Charging, Touch Controls, Water Resistance, IPX4, Active Noise Cancelling, Spatial Audio',
                                  'speciality': 'best iPhone, best sounding upper-mid range price',
                                  'codecs': 'AAC',
                                  'app support': 'Yes, Apple AirPods app',
                                  'battery life': 6},
    'Bang & Olufsen Beoplay EX': {'brand': 'Bang & Olufsen',
                                  'price': 775.00,
                                  'speciality': 'Most expensive, great-looking, nice sound',
                                  'functions': 'Bluetooth 5.2, Wireless Charging, IPX4, Water Resistance, Touch Controls, Active Noise Cancellation',
                                  'codecs': ['AAC', 'aptX Adaptive', 'SBC'],
                                  'app support': 'Bang & Olufsen app',
                                  'battery life': 8},
    'Beats Fit Pro': {'brand': 'Beats',
                      'price': 199.95,
                      'functions': 'Bluetooth 5.0, Wireless Charging, touch controls, Water Resistance, IPX7, Active Noise Cancelling, Ambient Sound, Auto Pause/Play',
                      'speciality': 'best workout',
                      'codecs': ['AAC', 'SBC'],
                      'app support': 'Yes, Beats app',
                      'battery life': 7},
    'Earfun Air Pro 3': {'brand': 'Earfun',
                         'price': 79.99,
                         'speciality': 'best value for money, good all-rounder',
                         'functions': 'Bluetooth 5.2, Wireless Charging, IPX5, Water Resistance, Touch Controls, Active Noise Cancelling',
                         'codecs': ['AAC', 'SBC'],
                         'app support': 'EarFun app',
                         'battery life': 9},
    'EPOS GTW 270 Hybrid': {'brand': 'EPOS',
                            'price': 239.00,
                            'functions': 'Bluetooth 5.1, aptX Low Latency, Touch Controls, Water Resistance, IPX5',
                            'speciality': 'best',
                            'codecs': ['AAC', 'aptX', 'SBC'],
                            'app support': 'No',
                            'battery life': 5},
    'Jabra Elite 7 Active': {'brand': 'Jabra',
                             'price': 279.99,
                             'functions': 'Bluetooth 5.2, Wireless Charging, Touch Controls, Water Resistance, IP57, Active Noise Cancelling, Ambient Sound, Adjustable EQ',
                             'speciality': 'best versatility, best for fitness',
                             'codecs': ['SBC', 'AAC'],
                             'app support': 'Yes, Jabra app',
                             'battery life': 9},
    'Jabra Elite 7 Pro': {'brand': 'Jabra',
                          'price': 329.99,
                          'functions': 'Bluetooth 5.2, Wireless Charging, Touch Controls, Water Resistance, IP57, Active Noise Cancelling, Adjustable EQ',
                          'speciality': 'best sounding in lower-mid range price',
                          'codecs': ['SBC', 'AAC'],
                          'app support': 'Yes, Jabra app',
                          'battery life': 9},
    'Jabra Elite 85t': {'brand': 'Jabra',
                        'price': 199.95,
                        'speciality': 'best Bluetooth codec support',
                        'functions': 'Bluetooth 5.1, Wireless Charging, IPX4, Water Resistance, Touch Controls, Active Noise Cancelling, Adjustable EQ',
                        'codecs': ['SBC', 'AAC', 'aptX'],
                        'app support': 'Jabra app',
                        'battery life': 5.5},
    'Nothing Ear 1': {'brand': 'Nothing',
                      'price': 99.99,
                      'speciality': 'best for design',
                      'functions': 'Bluetooth 5.2, Wireless Charging, IPX4, Water Resistance, Touch Controls, Ambient Sound',
                      'codecs': ['AAC', 'SBC'],
                      'app support': 'Yes',
                      'battery life': 5},
    'Samsung Galaxy Buds 2 Pro': {'brand': 'Samsung',
                                  'price': 379.00,
                                  'functions': 'Bluetooth 5.2, Wireless Charging, Touch Controls, Water Resistance, IPX7, Active Noise Cancelling, Ambient Sound',
                                  'speciality': 'best all-rounded, affordable',
                                  'codecs': ['SBC', 'AAC', 'Samsung Scalable'],
                                  'app support': 'Yes, Samsung Wearables app',
                                  'battery life': 8},
    'Sennheiser Momentum True Wireless 3': {'brand': 'Sennheiser',
                                            'price': 199.95,
                                            'speciality': 'best for bass lovers',
                                            'functions': 'Bluetooth 5.2, Wireless Charging, IPX4, Water Resistance, Touch Controls, Adjustable EQ',
                                            'codecs': ['AAC', 'aptX', 'SBC'],
                                            'app support': 'Sennheiser Smart Control app',
                                            'battery life': 7},
    'Sony WF-1000XM4': {'brand': 'Sony',
                        'price': 449.95,
                        'functions': 'Bluetooth 5.2, Wireless Charging, Touch Controls, Water Resistance, IPX4, Active Noise Cancelling, speak-to-chat, 360 Reality Audio',
                        'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support',
                        'codecs': ['SBC', 'AAC', 'LDAC'],
                        'app support': 'Yes, Sony Headphones Connect app',
                        'battery life': 8},
    'Sony WF-C500': {'brand': 'Sony',
                     'price': 115.00,
                     'speciality': 'best sounding cheapest',
                     'functions': 'Bluetooth 5.2, IPX4, Water Resistance, Touch Controls',
                     'codecs': ['AAC', 'SBC'],
                     'app support': 'Sony Headphones Connect app',
                     'battery life': 10}
}


# lists for user preferences, will be used in functions below
brand_list = ['Anker', 'Apple', 'Bang & Olufsen', 'Beats', 'Belkin', 'Bose', 'Bowers & Wilkins', 'Edifier', 'EPOS',
              'Jabra', 'Logitech', 'Nothing', 'Samsung', 'Sennheiser', 'Sony', 'N/A']

functions_list = ["Active Noise Cancelling", "Ambient Sound", "Auto Pause/Play", "Low Latency",
                  "Passive Noise Cancelling", "Quick Charge", "Voice Assistant", "Water Resistence",
                  "Wireless Charging",
                  "N/A"]
functions_desc_list = ["Reduces background noise while listening to music.",
                       "Allows hearing outside sounds while listening to music.",
                       "Stops/starts music playback when earbuds are removed/put on.",
                       "Reduces audio delay for better audio-video synchronization.",
                       "Blocks external sounds by physical design instead of using technology.",
                       "Can receive charging voltage at least 5V 2A",
                       "Can use voice commands like Siri or Google Assistant.",
                       "Can withstand exposure to water/sweat/rain to a certain degree.",
                       "Can charge wirelessly.",
                       "N/A"]

codec_list = ["AAC", "aptX", "aptX Low Latency", "aptX Adaptive", "aptX HD", "LC3", "LDAC", "LHDC", "SBC", "N/A"]

app_support_list = ["Yes", "No", "N/A"]

# set initial values
price_min = 0.00
price_max = 0.00
brand = "N/A"
codec = "N/A"
app_support = "N/A"
battery = "N/A"
functions = "N/A"
min_price = min([item["price"] for item in [*headphone_dict.values(), *earbud_dict.values()]])


# Category: let user choose which kind of headphone
def category_fc():
    global chosen_dict
    try:
        category_choice = input("Which category are you looking for? (Enter 'over-ear' or 'in-ear' or 'both'): ")
        if category_choice.lower() == "over-ear":
            chosen_dict = headphone_dict
            return chosen_dict
        elif category_choice.lower() == "in-ear":
            chosen_dict = earbud_dict
            return chosen_dict
        elif category_choice.lower() == "both":
            chosen_dict = headphone_dict | earbud_dict
            return chosen_dict
        else:
            print("Invalid choice!")
            category_fc()
    except ValueError:
        print("Invalid input! Please type over-ear / in-ear / both!")
        category_fc()


# Price range: user enter price range of product
def price_min_fc():
    global price_min
    try:
        price_min = int(input("Enter minimum price of the product (e.g. 100): "))
        if price_min < 0:
            print("You can't enter negative digits. Try again.")
            price_min_fc()
        else:
            price_min = round((float(price_min)), 2)
            price_max_fc()
        return price_min
    except ValueError:
        print("Invalid choice!")
        price_min_fc()


def price_max_fc():
    global price_max
    try:
        price_max = int(input("Enter maximum price of the product (e.g. 100): "))
        if price_max < price_min:
            print("Maximum price must not be smaller minimum price.")
            price_min_fc()
        elif price_max <= 0:
            print("Maximum price must be greater than $0.")
            price_min_fc()
        else:
            price_max = round((float(price_max)), 2)
            return price_max
    except ValueError:
        print("Invalid choice!")
        price_max_fc()


# Value check price user input
def price_check_fc():
    filtered_products = []
    for key, product_info in chosen_dict.items():
        formatted_value = round((product_info['price']), ndigits=2)
        product_info['price'] = formatted_value
        if price_min <= product_info['price'] <= price_max:
            filtered_products.append(key)
    if not filtered_products:
        print('Sorry, we dont have the product that meet your preferences.')
        return restart_fc()
    else:
        return filtered_products


# Function allows user to choose multiple specification
def mult_choice_fc(a, a_list):
    while True:
        choice_list = []
        print(f"Choose a {a} from the following: ")
        for i, _ in enumerate(a_list):
            choice_list.append(a_list[i])  # append the brand name
            if a == 'function':
                print(f"{i + 1}. {a_list[i]} - {functions_desc_list[i]}")
            else:
                print(f"{i + 1}. {a_list[i]}")
        user_input = input("Enter number of your choice (e.g. 1): ")
        user_list = user_input.split(", ")
        chosen_variables = []  # use a list to store multiple choices
        for i in user_list:
            try:
                choice_index = int(i) - 1  # convert user input to integer and subtract 1 to get the index
                if 0 <= choice_index < len(a_list):
                    chosen_variables.append(a_list[choice_index])
                else:
                    print(f"Invalid choice: {i}")
                    break
            except ValueError:
                print(f"Invalid input: {i}")
                break
        if len(chosen_variables) == len(user_list):
            break
    print(chosen_variables)
    return chosen_variables


# Filtering function to filter out products that does not meet user requirement
def filter_fc(choice, value, chosen_dict, filtered_products):
    to_remove = []
    for product in filtered_products:
        if product not in chosen_dict:
            continue
        if choice == ['N/A']:
            break
        if value == 'brand':
            if chosen_dict[product][value] not in choice:
                to_remove.append(product)
        else:
            if not all(c in chosen_dict[product][value] for c in choice):
                to_remove.append(product)

    filtered_products = [p for p in filtered_products if p not in to_remove]

    if not filtered_products:
        print('Sorry, we dont have the product that meet your preferences.')
        return restart_fc()
    else:
        return filtered_products


# Restarting function: In any state of the program, if no products meet user requirement, it will ask user if they would
#                      like to restart the whole program
def restart_fc():
    restart_input = input('Would you like to restart (eg. yes)? ')
    if restart_input.lower() == 'yes':
        recommendation()
    elif restart_input.lower() == 'no':
        return sys.exit()
    else:
        print('Please type yes or no.')
        return restart_fc()


# App support: choice on having app support or not
def app_support_fc():
    global app_support
    try:
        print("Would you like the headphone/earbud to include app support?")
        for i, n in enumerate(app_support_list):
            print(f"{i + 1}. {n}")
        app_support_choice = int(input("Enter your choice (e.g. 1): "))
        if app_support_choice <= 0 or app_support_choice > len(app_support_list):
            print("Invalid choice!")
            app_support_fc()
        else:
            app_support = app_support_list[app_support_choice - 1]
            return app_support
    except ValueError:
        print("Invalid choice!")
        app_support_fc()


# Battery Life: Battery life-long in hrs
def battery_life_fc():
    global battery
    try:
        battery = int(input("Enter minimum battery life without case charging in Hrs (e.g. 5): "))
        if battery <= 0:
            print("Invalid choice! Battery life cannot be 0 Hrs!")
            battery_life_fc()
        else:
            return battery
    except ValueError:
        print("Invalid choice!")
        battery_life_fc()


# Recommend product to user by filtering preferences
def recommendation():
    # Get user preferences by calling functions
    category_fc()
    price_min_fc()
    filtered_products = price_check_fc()  # putting return values into the filter_products list
    brand_choice = mult_choice_fc('brand', brand_list)
    filtered_products = filter_fc(brand_choice, 'brand', chosen_dict, filtered_products)
    function_choice = mult_choice_fc('function', functions_list)
    filtered_products = filter_fc(function_choice, 'functions', chosen_dict, filtered_products)
    codec_choice = mult_choice_fc('codec', codec_list)
    filtered_products = filter_fc(codec_choice, 'codecs', chosen_dict, filtered_products)
    app_support_fc()
    battery_life_fc()

    # final check if there are no products meeting requirement
    if bool(filtered_products) == 0:
        print('Sorry, we dont have the product that meet your preferences.')
        restart_fc()
    else:
        print("\nHere is the recommended products: "
              f"{filtered_products}\n")
        return restart_fc()


print('Hello there! I am the True Wireless Headphone/Earbud recommendation program.\n'
      'I am here to help you choose wireless headphones that best suits your preferences.\n'
      'Before we continue, there are a few things you should know: \n'
      '1. N/A in choices means you have no requirements about that specific preference or select all.\n'
      '2. In multiple choices, please input in format (eg. 1, 2, 3); Other questions input numbers only (eg. 1)\n'
      '3. Please only input "N/A" if so.'
      f'4. Lowest price of all headphones is ${min_price}. Please enter a price higher than that.\n'
      # 'Before we continue, please be noted that you are going to be redirected to Versus.com for generating the outcome.\n'
      # 'Please make sure you are connected to an active internet.\n'
      )
recommendation()
