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

# dictionary for options - includes price, brand, functions, Bluetooth Codec, App support, Battery Life and Speciality
# need to add the options one by one
headphone_dict = {
    'Sony WH-1000XM5': {'brand': 'Sony',
                        'price': 539.99,
                        'functions': 'Active Noise Cancelling, Ambient Sound, Voice Assistant',
                        'codecs': 'LDAC, aptX, AAC',
                        'app support': 'Yes',
                        'battery life': 'More than 20 hours'},
    'Apple Airpods Max': {'brand': 'Apple',
                          'price': 899.00,
                          'functions': 'Active Noise Cancelling, Transparency mode',
                          'codecs': 'AAC',
                          'app support': 'No',
                          'battery life': '10-20 hours'},
    'Sony WH-1000XM4': {'brand': 'Sony',
                        'price': 429.99,
                        'functions': 'Active Noise Cancelling, Ambient Sound, Voice Assistant',
                        'codecs': 'LDAC, aptX, AAC',
                        'app support': 'Yes',
                        'battery life': 'More than 20 hours'},
    'Bose Noise Cancelling Headphones 700': {'brand': 'Bose',
                                             'price': 679.00,
                                             'functions': 'Active Noise Cancelling, Voice Assistant',
                                             'codecs': 'SBC, AAC',
                                             'app support': 'Yes',
                                             'battery life': '10-20 hours'},
    'Logitech G435 LIGHTSPEED Wireless': {'brand': 'Logitech',
                                          'price': 159.99,
                                          'functions': 'Gaming',
                                          'codecs': 'SBC, AAC',
                                          'app support': 'No',
                                          'battery life': '10-20 hours'},
    'Bowers & Wilkins Px7 S2 Headphones': {'brand': 'Bowers & Wilkins',
                                           'price': 749.99,
                                           'functions': 'Active Noise Cancelling, Ambient Sound',
                                           'codecs': 'aptX Adaptive, aptX HD, AAC, SBC',
                                           'app support': 'Yes',
                                           'battery life': 'More than 20 hours'},
    'Sennheiser Momentum 4 Wireless': {'brand': 'Sennheiser',
                                       'price': 679.95,
                                       'functions': 'Active Noise Cancelling, Transparent Hearing, Voice Assistant',
                                       'codecs': 'SBC, AAC, aptX, aptX Low Latency, LHDC',
                                       'app support': 'Yes',
                                       'battery life': '10-20 hours'},
    'Belkin Soundform Mini': {'brand': 'Belkin',
                              'price': 99.99,
                              'functions': 'Wireless, Voice Assistant',
                              'codecs': 'SBC, AAC',
                              'app support': 'Yes',
                              'battery life': '10-20 hours'},
    'Anker SoundCore Life Q30': {'brand': 'Anker',
                                 'price': 159.99,
                                 'functions': 'Active Noise Cancelling, Voice Assistant',
                                 'codecs': 'SBC, AAC',
                                 'app support': 'No',
                                 'battery life': 'More than 20 hours'},
    'Edifier W820NB': {'brand': 'Edifier',
                       'price': 159.99,
                       'functions': 'Active Noise Cancelling, Voice Assistant',
                       'codecs': 'SBC, AAC',
                       'app support': 'Yes',
                       'battery life': 'More than 20 hours'},
}

earbud_dict = {
    'Samsung Galaxy Buds 2': {'brand': 'Samsung',
                              'price': 179.00,
                              'functions': 'Bluetooth 5.2, wireless charging, touch controls, water resistance (IPX7), active noise cancelling, ambient mode',
                              'speciality': 'best all-rounded, affordable',
                              'codecs': ['SBC', 'AAC', 'Samsung Scalable'],
                              'app support': 'Yes, Samsung Wearables app',
                              'battery life': '7.5 hours (buds), 29 hours (case)'},
    'Apple Airpods Pro (Gen 2)': {'brand': 'Apple',
                                  'price': 379.00,
                                  'functions': 'Bluetooth 5.0, wireless charging, touch controls, water resistance (IPX4), active noise cancelling, spatial audio',
                                  'speciality': 'best iPhone, best sounding upper-mid range price',
                                  'codecs': 'AAC',
                                  'app support': 'Yes, Apple AirPods app',
                                  'battery life': '4.5 hours (buds), 24 hours (case)'},
    'Beats Fit Pro': {'brand': 'Beats',
                      'price': 199.95,
                      'functions': 'Bluetooth 5.0, wireless charging, touch controls, water resistance (IPX7), active noise cancelling, transparency mode, automatic pause and play',
                      'speciality': 'best workout',
                      'codecs': ['AAC', 'SBC'],
                      'app support': 'Yes, Beats app',
                      'battery life': '9 hours (buds), 24 hours (case)'},
    'Sony WF-1000XM4': {'brand': 'Sony',
                        'price': 449.95,
                        'functions': 'Bluetooth 5.2, wireless charging, touch controls, water resistance (IPX4), active noise cancelling, speak-to-chat, 360 Reality Audio',
                        'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support',
                        'codecs': ['SBC', 'AAC', 'LDAC'],
                        'app support': 'Yes, Sony Headphones Connect app',
                        'battery life': '8 hours (buds), 24 hours (case)'},
    'Jabra Elite 7 Active': {'brand': 'Jabra',
                             'price': 279.99,
                             'functions': 'Bluetooth 5.2, wireless charging, touch controls, water resistance (IP57), active noise cancelling, transparency mode, adjustable EQ',
                             'speciality': 'best versatility, best for fitness',
                             'codecs': ['SBC', 'AAC'],
                             'app support': 'Yes, Jabra app',
                             'battery life': '9 hours (buds), 35 hours (case)'},
    'Jabra Elite 7 Pro': {'brand': 'Jabra',
                          'price': 329.99,
                          'functions': 'Bluetooth 5.2, wireless charging, touch controls, water resistance (IP57), active noise cancelling, adjustable EQ',
                          'speciality': 'best sounding in lower-mid range price',
                          'codecs': ['SBC', 'AAC'],
                          'app support': 'Yes, Jabra app',
                          'battery life': '9 hours (buds), 35 hours (case)'},
    'EPOS GTW 270 Hybrid': {'brand': 'EPOS',
                            'price': 329.00,
                            'functions': 'Bluetooth 5.1, aptX Low Latency, touch controls, water resistance (IPX5)',
                            'speciality': 'best',
                            'codecs': ['AAC', 'aptX', 'SBC'],
                            'app support': '',
                            'battery life': ''},

    'Nothing Ear 1': {'brand': 'Nothing',
                      'price': 99.99,
                      'speciality': 'best for design',
                      'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, transparent design',
                      'codecs': ['AAC', 'SBC'],
                      'app support': 'Yes',
                      'battery life': '5.7 hours (buds), 34 hours (case)'},
    'Sennheiser Momentum TW 3': {'brand': 'Sennheiser',
                                 'price': 199.95,
                                 'speciality': 'best for bass lovers',
                                 'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, equalizer customization',
                                 'codecs': ['AAC', 'aptX', 'SBC'],
                                 'app support': 'Sennheiser Smart Control app',
                                 'battery life': '7 hours (buds), 28 hours (case)'},
    'Earfun Air Pro 3': {'brand': 'Earfun',
                         'price': 79.99,
                         'speciality': 'best value for money, good all-rounder',
                         'functions': 'Bluetooth 5.2, wireless charging, IPX5 water resistance, touch controls, ANC',
                         'codecs': ['AAC', 'SBC'],
                         'app support': 'EarFun app',
                         'battery life': '7 hours (buds), 25 hours (case)'},
    'Bang & Olufsen Beoplay EX': {'brand': 'Bang & Olufsen',
                                  'price': 775.00,
                                  'speciality': 'Most expensive, great-looking, nice sound',
                                  'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, active noise cancellation',
                                  'codecs': ['AAC', 'aptX Adaptive', 'SBC'],
                                  'app support': 'Bang & Olufsen app',
                                  'battery life': '7.5 hours (buds), 20 hours (case)'},
    'Jabra Elite 85t': {'brand': 'Jabra',
                        'price': 199.95,
                        'speciality': 'best Bluetooth codec support',
                        'functions': 'Bluetooth 5.1, wireless charging, IPX4 water resistance, touch controls, ANC, adjustable EQ',
                        'codecs': ['SBC', 'AAC', 'aptX'],
                        'app support': 'Jabra app',
                        'battery life': '7 hours (buds), 24 hours (case)'},
    'Sony WF-C500': {'brand': 'Sony',
                     'price': 115.00,
                     'speciality': 'best sounding cheapest',
                     'functions': 'Bluetooth 5.2, IPX4 water resistance, touch controls',
                     'codecs': ['AAC', 'SBC'],
                     'app support': 'Sony Headphones Connect app',
                     'battery life': '9 hours (buds), 26 hours (case)'}
}


# Note: price and features of the headphones are subject to change over time, so the above information might not

brand_list = ['Anker', 'Apple', 'Bang & Olufsen', 'Beats', 'Belkin', 'Bose', 'Bowers & Wilkins', 'Edifier', 'EPOS',
              'Jabra', 'Logitech', 'Nothing', 'Samsung', 'Sennheiser', 'Sony', 'N/A']

functions_list = ["Active Noise Cancelling", "Ambient Sound", "Auto Pause/Play", "Low Latency",
                  "Passive Noise Cancelling", "Quick Charge", "Voice Call", "Water Resistence", "Wireless Charging",
                  "N/A"]

codec_list = ["AAC", "aptX", "aptX Low Latency", "aptX Adaptive", "aptX HD", "LC3", "LDAC", "LHDC", "SBC", "N/A"]

app_support_list = ["Yes", "No", "N/A"]

battery_list = ["Less than 5 hours", "5-10 hours", "10-20 hours", "More than 20 hours", "N/A"]

# set initial values
price_min = 0.00
price_max = 0.00
brand = "N/A"
codec = "N/A"
app_support = "N/A"
battery = "N/A"
functions = "N/A"


# Category - let user choose which kind of headphone
def category_fc():
    global chosen_dict
    try:
        category_choice = input("Which category are you looking for? (Enter 'headphone' or 'earbud' or 'both'): ")
        if category_choice.lower() == "headphone":
            chosen_dict = headphone_dict
            return  # print(chosen_dict)
        elif category_choice.lower() == "earbud":
            chosen_dict = earbud_dict
            return  # print(chosen_dict)
        elif category_choice.lower() == "both":
            chosen_dict = headphone_dict | earbud_dict
            return  # print(chosen_dict)
        else:
            print("Invalid choice!")
            category_fc()
    except ValueError:
        print("Invalid choice!")
        category_fc()


# Price range - user enter price range of product
def price_range_fc():
    global price_min, price_max
    n = 0
    try:
        price_min = float(input("Enter minimum price (e.g. 100): "))
        if price_min < 0:
            print("You can't enter negative digits. Try again.")
            price_range_fc()
        else:
            while n == 0:
                price_max = float(input("Enter maximum price (e.g. 100): "))
                if price_max < price_min:
                    print("Maximum price must not be smaller minimum price.")
                elif price_max <= 0:
                    print("Maximum price must be greater than $0.")
                else:
                    n = 1
        price_min = round((float(price_min)), ndigits=2)
        price_max = round((float(price_max)), ndigits=2)
        return price_min, price_max
    except ValueError:
        print("Invalid choice!")
        price_range_fc()


# Brand - brand of product
def brand_fc():
    global brand
    try:
        print("Choose a brand from the following: ")
        for i, n in enumerate(brand_list):
            print(f"{i + 1}. {n}")
        brand_choice = int(input("Enter your choice (e.g. 16): "))
        if brand_choice <= 0 or brand_choice > 16:
            print("Invalid choice!")
            brand_fc()
        else:
            brand = brand_list[brand_choice - 1]
            return print(brand)
    except ValueError:
        print("Invalid choice!")
        brand_fc()


# Functions - functions of product included
'''def functions_fc():
    try:
        functions_choices = ["Active Noise Cancelling", "Ambient Sound", "Auto Pause/Play", "Low Latency",
                             "Passive Noise Cancelling", "Quick Charge", "Voice Call", "Water Resistence", "Wireless Charging", "N/A"]
        functions = input("Here are some functions:\n - " + " \n - ".join(functions_choices) + "\nEnter functions: ").split(",")
        return functions == [f.strip() for f in functions]
    except ValueError:
        print("Invalid choice!")
        functions_fc()'''  # previous ver.


def functions_fc():
    global functions
    try:
        print("Choose a function from the following: ")
        for i, n in enumerate(functions_list):
            print(f"{i + 1}. {n}")
        functions_choice = int(input("Enter your choice (e.g. 10): "))
        if functions_choice <= 0 or functions_choice > 10:
            print("Invalid choice!")
            functions_fc()
        else:
            functions = functions_list[functions_choice - 1]
            return functions
    except ValueError:
        print("Invalid choice!")
        functions_fc()


# Support Codec - codec of product supported
def codec_fc():
    global codec
    try:
        print("Choose a codec from the following: ")
        for i, n in enumerate(codec_list):
            print(f"{i + 1}. {n}")
        codec_choice = int(input("Enter your choice (e.g. 10): "))
        if codec_choice <= 0 or codec_choice > 10:
            print("Invalid choice!")
            codec_fc()
        else:
            codec = codec_list[codec_choice - 1]
            return codec
    except ValueError:
        print("Invalid choice!")
        codec_fc()


# App support - choice on having app support or not
def app_support_fc():
    global app_support
    try:
        print("Would you like the headphone/earbud to include app support?")
        for i, n in enumerate(app_support_list):
            print(f"{i + 1}. {n}")
        app_support_choice = int(input("Enter your choice (e.g. 1): "))
        if app_support_choice <= 0 or app_support_choice > 3:
            print("Invalid choice!")
            app_support_fc()
        else:
            app_support = app_support_list[app_support_choice - 1]
            return app_support
    except ValueError:
        print("Invalid choice!")
        app_support_fc()


# Battery Life - Battery life-long in hrs
def battery_life_fc():
    global battery
    try:
        print("Please choose battery life long (in Hrs): ")
        for i, n in enumerate(battery_list):
            print(f"{i + 1}. {n}")
        battery_choice = int(input("Enter your choice (e.g. 1): "))
        if battery_choice <= 0 or battery_choice > 5:
            print("Invalid choice!")
            battery_life_fc()
        else:
            battery = battery_list[battery_choice - 1]
            return battery
    except ValueError:
        print("Invalid choice!")
        battery_life_fc()


# Speciality - Special or Honours E.g. Best value
'''def speciality_fc():
    global speciality
    speciality_choices = ["Value", "Cheapest", "Pricey", "Long Usage Hours", "Good Sounding (in price range)",
                          "Best ANC", "Best Ambient", "Best Overall"]
    return speciality == input("Enter speciality (" + ", ".join(speciality_choices) + "): ")'''


# speciality = speciality_fc()


# Recommend product to user by filtering preferences
def recommendation():
    filtered_products = []

    # Get user preferences, call previous functions
    category_fc()
    price_range_fc()
    brand_fc()
    functions_fc()
    codec_fc()
    app_support_fc()
    battery_life_fc()
    # print(price_min, price_max, brand, functions, codec, app_support, battery)
    # print(price_min, price_max, type(price_min), type(price_max))
    # Filter products based on user choices
    for key, product_info in chosen_dict.items():
        formatted_value = round((product_info['price']), ndigits=2)
        product_info['price'] = formatted_value
        if price_min <= product_info['price'] <= price_max:
            # print('True')
            # print(brand, type(brand))
            # print(brand)
            # print((product_info['brand']))
            # print((brand in product_info['brand']))
            if (brand in product_info['brand']) or (brand == "N/A"):
                # print('True')
                if (functions in product_info['functions']) or (functions == "N/A"):
                    # print('True')
                    if (codec in product_info['codecs']) or (codec == "N/A"):
                        # print('True')
                        if (app_support == "N/A") or (app_support in product_info['app support']):
                            # print('True')
                            if (battery == "N/A") or (battery.lower() in product_info['battery life']):
                                # print('True')
                                filtered_products.append(key)
        # else:
        # print("False")
    if bool(filtered_products) == 0:
        print("Sorry, we dont have the product that meet your enquirement.")
    else:
        print("Here is the recommended products: "
              f"{filtered_products}")


recommendation()  # price_min, price_max, brand, functions, codec

'''   
21-03
earbud_dict = {'Samsung Galaxy Buds 2': {'brand': 'Samsung', 'price': 149.99, 'speciality': 'best all rounded',
'codecs': ['SBC', 'AAC', 'Samsung Scalable'], 'app support': 'Galaxy Wearable app',
'battery life': '5 hours (buds), 20 hours (case)'},
'Apple Airpods Pro (Gen 2)': {'brand': 'Apple', 'price': 249.00,
'speciality': 'best iPhone, best sounding upper-mid range price, expensive',
'codecs': ['AAC'], 'app support': 'Apple Airpods app',
'battery life': '4.5 hours (buds), 24 hours (case)'},
'Beats Fit Pro': {'brand': 'Beats', 'price': 149.99, 'speciality': 'best workout',
'codecs': ['AAC', 'SBC'], 'app support': 'Beats app',
'battery life': '7 hours (buds), 18 hours (case)'},
'Sony WF-1000XM4': {'brand': 'Sony', 'price': 279.99,
'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support',
'codecs': ['SBC', 'AAC', 'LDAC'], 'app support': 'Sony Headphones Connect app',
'battery life': '8 hours (buds), 24 hours (case)'},
'Jabra Elite 7 Active': {'brand': 'Jabra', 'price': 179.99, 'speciality': 'best versatility',
'codecs': ['SBC', 'AAC'], 'app support': 'Jabra app',
'battery life': '9 hours (buds), 35 hours (case)'},
'Jabra Elite 7 Pro': {'brand': 'Jabra', 'price': 199.99,
'speciality': 'best sounding in lower-mid range price',
'codecs': ['SBC', 'AAC'], 'app support': 'Jabra app',
'battery life': '9 hours (buds), 35 hours (case)'},
'EPOS GTW 270 Hybrid': {'brand': 'EPOS', 'price': 199.00, 'speciality': 'best gaming',
'codecs': ['SBC', 'AAC', 'aptX Low Latency'], 'app support': 'EPOS Gaming Suite app',
'battery life': '5 hours (buds), 20 hours (case)'},
'Nothing Ear 1': {'brand': 'Nothing', 'price': 99.99, 'speciality': 'best for design',
'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, transparent design',
'codecs': 'AAC, SBC'},
'Sennheiser Momentum TW 3': {'brand': 'Sennheiser', 'price': 199.95, 'speciality': 'best for bass lovers',
'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, equalizer customization',
'codecs': 'AAC, aptX, SBC'},
'Earfun Air Pro 3': {'brand': 'Earfun', 'price': 79.99,
'speciality': 'best value for money, good all-rounder',
'functions': 'Bluetooth 5.2, wireless charging, IPX5 water resistance, touch controls, ANC',
'codecs': 'AAC, SBC'},
'Bang & Ol


headphone_dict = {
'Sony WH-1000XM5': {'brand': 'Sony', 'price': 595.00, 'functions': 'Active Noise Cancelling, Ambient Sound',
'speciality': 'best all rounded, best ANC, comfortable', 'codec': 'LDAC, AAC, SBC',
'app support': 'Sony Headphones Connect', 'battery life': '30 hours'},
'Apple Airpods Max': {'brand': 'Apple', 'price': 999.00,
'speciality': 'best iphone, 2nd most expensive, 2nd best for workout', 'codec': 'AAC, SBC',
'app support': 'Apple Music, Find My', 'battery life': '20 hours'},
'Sony WH-1000XM4': {'brand': 'Sony', 'price': 414.00,
'speciality': 'best sounding bass, best for workout, Best Bluetooth codec support',
'codec': 'LDAC, AAC, SBC', 'app support': 'Sony Headphones Connect', 'battery life': '30 hours'},
'Bose Noise Cancelling Headphones 700': {'brand': 'Bose', 'price': 699.95, 'speciality': 'best phone call',
'codec': 'AAC, SBC', 'app support': 'Bose Music', 'battery life': '20 hours'},
'Logitech G435 LIGHTSPEED Wireless': {'brand': 'Logitech', 'price': 249.90, 'speciality': 'best budget gaming',
'codec': 'SBC', 'app support': 'Logitech G HUB', 'battery life': '18 hours'},
'Bowers & Wilkins Px7 S2 Headphones': {'brand': 'Bowers & Wilkins', 'price': 649.00,
'speciality': 'best look, most comfort, 3rd best Bluetooth codec support',
'codec': 'aptX Adaptive, aptX HD, aptX Classic, AAC, SBC',
'app support': 'Bowers & Wilkins Headphones app', 'battery life': '30 hours'},
'Sennheiser Momentum 4 Wireless': {'brand': 'Sennheiser', 'price': 599.95,
'speciality': '2nd best sounding bass, 2nd best Bluetooth codec support',
'codec': 'AAC, aptX


 
16-03
if chosen_dict == headphone_dict:
    category_name = "headphones"
else:
    category_name = "earbuds"
    
recommended_list = []

for product, features in chosen_dict.items():
    if price_min <= features['price'] <= price_max and (brand == "N/A" or features['brand'] == brand) and (codec == "N/A" or codec in features['speciality']):
        if app_support != "N/A":
            if app_support == "Yes":
                if "app support" in features and features["app support"] == True:
                    recommended_list.append(product)
            elif app_support == "No":
                if "app support" not in features or features["app support"] == False:
                    recommended_list.append(product)
        else:
            recommended_list.append(product)

if len(recommended_list) == 0:
    return "No product found matching the criteria"
else:
    output = f"Recommended {category_name} within the price range ${price_min} to ${price_max} and with {brand} brand, {codec} codec support, {app_support} app support, {battery} battery life and {functions} functions: "
    output += ", ".join(recommended_list)
    return output

if len(filtered_products) == 0:
        print("No products found with the given preferences!")
    else:
        print("Here are the products that match your preferences:")
        for product in filtered_products:
            print(product)

# Initialize list of recommendations
    recommendations = []

    # Loop through headphones and earbuds dictionaries to find matches
    for product_dict in [headphone_dict, earbud_dict]:
        for key, price in product_dict.items():
            # Filter by price range
            if price_min <= price <= price_max:
                print(key)
                recommendations.append(key)
    return recommendations

# Filter by brand
                if brand.lower() in product.lower():
                    # Filter by functions
                    if all(f.lower() in product.lower() for f in functions):
                        # Filter by codec support
                        if ('AAC' in codec and 'AAC' in product_dict[product].get('codec', '')) or \
                                ('SBC' in codec and 'SBC' in product_dict[product].get('codec', '')) or \
                                ('LDAC' in codec and 'LDAC' in product_dict[product].get('codec', '')):
                            recommendations.append(product)'''  # unused code
'''
22-03
# define a list of options
options = ['option 1', 'option 2', 'option 3', 'option 4']

# display the options and let the user select multiple options
selected_options = []
print("Please select your options (separated by commas):")
for i, option in enumerate(options):
    print(f"{i+1}. {option}")
selected_indices = input().split(',')
for index in selected_indices:
    selected_options.append(options[int(index)-1])

# print the selected options
print("You have selected:")
for option in selected_options:
    print(option)

earbud_dict = {
    'Samsung Galaxy Buds 2': {'brand': 'Samsung',
                              'price': 149.99,
                              'functions' '',
                              'speciality': 'best all rounded',
                              'codecs': ['SBC', 'AAC', 'Samsung Scalable'],
                              'app support': 'Yes',
                              'battery life': '5 hours (buds), 20 hours (case)'},
    'Apple Airpods Pro (Gen 2)': {'brand': 'Apple',
                                  'price': 249.00,
                                  'functions': '',
                                  'speciality': 'best iPhone, best sounding upper-mid range price, expensive',
                                  'codecs': 'AAC',
                                  'app support': 'Yes',
                                  'battery life': '4.5 hours (buds), 24 hours (case)'},
    'Beats Fit Pro': {'brand': 'Beats',
                      'price': 149.99,
                      'functions': '',
                      'speciality': 'best workout',
                      'codecs': ['AAC', 'SBC'],
                      'app support': 'Beats app',
                      'battery life': '7 hours (buds), 18 hours (case)'},
    'Sony WF-1000XM4': {'brand': 'Sony',
                        'price': 279.99,
                        'functions': 'Active Noise Cancelling',
                        'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support',
                        'codecs': ['SBC', 'AAC', 'LDAC'],
                        'app support': 'Sony Headphones Connect app',
                        'battery life': '8 hours (buds), 24 hours (case)'},
    'Jabra Elite 7 Active': {'brand': 'Jabra',
                             'price': 179.99,
                             'functions': '',
                             'speciality': 'best versatility',
                             'codecs': ['SBC', 'AAC'],
                             'app support': 'Jabra app',
                             'battery life': '9 hours (buds), 35 hours (case)'},
    'Jabra Elite 7 Pro': {'brand': 'Jabra',
                          'price': 199.99,
                          'functions': '',
                          'speciality': 'best sounding in lower-mid range price',
                          'codecs': ['SBC', 'AAC'],
                          'app support': 'Jabra app',
                          'battery life': '9 hours (buds), 35 hours (case)'},
    'EPOS GTW 270 Hybrid': {'brand': 'EPOS',
                            'price': 199.00,
                            'functions': '',
                            'speciality': 'best gaming',
                            'codecs': ['SBC', 'AAC', 'aptX Low Latency'],
                            'app support': 'EPOS Gaming Suite app',
                            'battery life': '5 hours (buds), 20 hours (case)'},
    'Nothing Ear 1': {'brand': 'Nothing',
                      'price': 99.99, 'speciality': 'best for design',
                      'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, transparent design',
                      'codecs': ['AAC, SBC'],
                      'app support': 'Yes',
                      'battery life': ''},
    'Sennheiser Momentum TW 3': {'brand': 'Sennheiser', 'price': 199.95,
                                 'speciality': 'best for bass lovers',
                                 'functions': 'Bluetooth 5.2, wireless charging, IPX4 water resistance, touch controls, equalizer customization',
                                 'codecs': ['AAC', 'aptX', 'SBC']},
    'Earfun Air Pro 3': {'brand': 'Earfun',
                         'price': 79.99,
                         'speciality': 'best value for money, good all-rounder',
                         'functions': 'Bluetooth 5.2, wireless charging, IPX5 water resistance, touch controls, ANC',
                         'codecs': 'AAC, SBC'},
    'Bang & Olufsen Beoplay EX': {'brand': 'Bang & Olufsen',
                                  'price': 775.00,
                                  'speciality': 'Most expensive, great-looking, nice sound'},
    'Jabra Elite 85t': {'brand': 'Jabra',
                        'price': 199.95,
                        'speciality': 'best Bluetooth codec support'},
    'Sony WF-C500': {'brand': 'Sony',
                     'price': 115.00,
                     'functions': '',
                     'speciality': 'best sounding cheapest'},
}

21-03
headphone_dict = {
    'Sony WH-1000XM5': {'brand': 'Sony', 'price': 595.00, 'functions': 'Active Noise Cancelling, Ambient Sound',
                        'speciality': 'best all rounded, best ANC, comfortable'},
    'Apple Airpods Max': {'brand': 'Apple', 'price': 999.00,
                          'speciality': 'best iphone, 2nd most expensive, 2nd best for workout'},
    'Sony WH-1000XM4': {'brand': 'Sony', 'price': 414.00,
                        'speciality': 'best sounding bass, best for workout, Best Bluetooth codec support'},
    'Bose Noise Cancelling Headphones 700': {'brand': 'Bose', 'price': 699.95, 'speciality': 'best phone call'},
    'Logitech G435 LIGHTSPEED Wireless': {'brand': 'Logitech', 'price': 249.90, 'speciality': 'best budget gaming'},
    'Bowers & Wilkins Px7 S2 Headphones': {'brand': 'Bowers & Wilkins', 'price': 649.00,
                                           'speciality': 'best look, most comfort, 3rd best Bluetooth codec support'},
    'Sennheiser Momentum 4 Wireless': {'brand': 'Sennheiser', 'price': 599.95,
                                       'speciality': '2nd best sounding bass, 2nd best Bluetooth codec support'},
    'Belkin Soundform Mini': {'brand': 'Belkin', 'price': 59.99, 'speciality': 'best for kids'},
    'Anker SoundCore Life Q30': {'brand': 'Anker', 'price': 241.95, 'speciality': 'best value'},
    'Edifier W820NB': {'brand': 'Edifier', 'price': 168.00, 'speciality': 'best sounding cheapest'},
    }

earbud_dict = {'Samsung Galaxy Buds 2': {'brand': 'Samsung', 'price': 279.00, 'speciality': 'best all rounded'},
               'Apple Airpods Pro (Gen 2)': {'brand': 'Apple', 'price': 479.00,
                                             'speciality': 'best iphone, best sounding upper-mid range price, expensive'},
               'Beats Fit Pro': {'brand': 'Beats', 'price': 349.95, 'speciality': 'best workout'},
               'Sony WF-1000XM4': {'brand': 'Sony', 'price': 369.00,
                                   'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support'},
               'Jabra Elite 7 Active': {'brand': 'Jabra', 'price': 284.00, 'speciality': 'best versatility'},
               'Jabra Elite 7 Pro': {'brand': 'Jabra', 'price': 296.00,
                                     'speciality': 'best sounding in lower-mid range price'},
               'EPOS GTW 270 Hybrid': {'brand': 'EPOS', 'price': 239.00, 'speciality': 'best gaming'},
               'Nothing Ear 1': {'brand': 'Nothing', 'price': 189.00, 'speciality': 'best looking'},
               'Sennheiser Momentum TW 3': {'brand': 'Sennheiser', 'price': 378.00, 'speciality': 'best sounding bass'},
               'Earfun Air Pro 3': {'brand': 'Earfun', 'price': 139.00,
                                    'speciality': 'best value, good-looking, all rounded'},
               'Bang & Olufsen Beoplay EX': {'brand': 'Bang & Olufsen', 'price': 775.00,
                                             'speciality': 'Most expensive, great-looking, nice sound'},
               'Jabra Elite 85t': {'brand': 'Jabra', 'price': 199.95, 'speciality': 'best Bluetooth codec support'},
               'Sony WF-C500': {'brand': 'Sony', 'price': 115.00, 'speciality': 'best sounding cheapest'},
               }

16-03
headphone_list = [    ['Sony WH-1000XM5', 'Sony', 595.00, 'best all rounded, best ANC, comfortable'],
    ['Apple Airpods Max', 'Apple', 999.00, 'best iphone, 2nd most expensive, 2nd best for workout'],
    ['Sony WH-1000XM4', 'Sony', 414.00, 'best sounding bass, best for workout, Best Bluetooth codec support'],
    ['Bose Noise Cancelling Headphones 700', 'Bose', 699.95, 'best phone call'],
    ['Logitech G435 LIGHTSPEED Wireless', 'Logitech', 249.90, 'best budget gaming'],
    ['Bowers & Wilkins Px7 S2 Headphones', 'Bowers & Wilkins', 649.00, 'best look, most comfort, 3rd best Bluetooth codec support'],
    ['Sennheiser Momentum 4 Wireless', 'Sennheiser', 599.95, '2nd best sounding bass, 2nd best Bluetooth codec support'],
    ['Belkin Soundform Mini', 'Belkin', 59.99, 'best for kids'],
    ['Anker SoundCore Life Q30', 'Anker', 241.95, 'best value'],
    ['Edifier W820NB', 'Edifier', 168.00, 'best sounding cheapest']
]


09-03:
# Headphone/Earbuds Recommendation Program

headphone_dict = {'Sony WH-1000XM5': {'price': 595.00, 'speciality': 'best all rounded, best ANC, comfortable'},  
                  'Apple Airpods Max': {'price': 999.00, 'speciality': 'best iphone, 2nd most expensive, 2nd best for workout'},  
                  'Sony WH-1000XM4': {'price': 414.00, 'speciality': 'best sounding bass, best for workout, Best Bluetooth codec support'},  
                  'Bose Noise Cancelling Headphones 700': {'price': 699.95, 'speciality': 'best phone call'},  
                  'Logitech G435 LIGHTSPEED Wireless': {'price': 249.90, 'speciality': 'best budget gaming'},  
                  'Bowers & Wilkins Px7 S2 Headphones': {'price': 649.00, 'speciality': 'best look, most comfort, 3rd best Bluetooth codec support'},  
                  'Sennheiser Momentum 4 Wireless': {'price': 599.95, 'speciality': '2nd best sounding bass, 2nd best Bluetooth codec support'},  
                  'Belkin Soundform Mini': {'price': 59.99, 'speciality': 'best for kids'},  
                  'Anker SoundCore Life Q30': {'price': 241.95, 'speciality': 'best value'},  
                  'Edifier W820NB': {'price': 168.00, 'speciality': 'best sounding cheapest'},  
                  }

earbud_dict = {'Samsung Galaxy Buds 2': {'price': 279.00, 'speciality': 'best all rounded'},  
               'Apple Airpods Pro (Gen 2)': {'price': 479.00, 'speciality': 'best iphone, best sounding upper-mid range price, expensive'},  
               'Beats Fit Pro': {'price': 349.95, 'speciality': 'best workout'},  
               'Sony WF-1000XM4': {'price': 369.00, 'speciality': 'best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support'},  
               'Jabra Elite 7 Active': {'price': 284.00, 'speciality': 'best versatility'},  
               'Jabra Elite 7 Pro': {'price': 296.00, 'speciality': 'best sounding in lower-mid range price'},  
               'EPOS GTW 270 Hybrid': {'price': 239.00, 'speciality': 'best gaming'},  
               'Nothing Ear 1': {'price': 189.00, 'speciality': 'best looking'},  
               'Sennheiser Momentum TW 3': {'price': 378.00, 'speciality': 'best sounding bass'},  
               'Earfun Air Pro 3': {'price': 139.00, 'speciality': 'best value, good-looking, all rounded'},  
               'Bang & Olufsen Beoplay EX': {'price': 775.00, 'speciality': 'Most expensive, great-looking, nice sound'},  
               'Jabra Elite 85t': {'price': 199.95, 'speciality': 'best Bluetooth codec support'},  
               'Sony WF-C500': {'price': 115.00, 'speciality': 'best sounding cheapest'},  
                }

# Price range
price_range = input("Enter price range (e.g. 100-500): ").split("-")


# Headphone/Earbuds Recommendation Program

headphone_dict = {'Sony WH-1000XM5': 595.00,  
                  'Apple Airpods Max': 999.00,  
                  'Sony WH-1000XM4': 414.00,  
                  'Bose Noise Cancelling Headphones 700': 699.95,  
                  'Logitech G435 LIGHTSPEED Wireless': 249.90,  
                  'Bowers & Wilkins Px7 S2 Headphones': 649.00,  
                  'Sennheiser Momentum 4 Wireless': 599.95,  
                  'Belkin Soundform Mini': 59.99,  
                  'Anker SoundCore Life Q30': 241.95,  
                  'Edifier W820NB': 168.00,  
                  }

earbud_dict = {'Samsung Galaxy Buds 2': 279.00,  
               'Apple Airpods Pro (Gen 2)': 479.00,  
               'Beats Fit Pro': 349.95,  
               'Sony WF-1000XM4': 369.00,  
               'Jabra Elite 7 Active': 284.00,  
               'Jabra Elite 7 Pro': 296.00,  
               'EPOS GTW 270 Hybrid': 239.00,  
               'Nothing Ear 1': 189.00,  
               'Sennheiser Momentum TW 3': 378.00,  
               'Earfun Air Pro 3': 139.00,  
               'Bang & Olufsen Beoplay EX': 775.00,  
               'Jabra Elite 85t': 199.95,  
               'Sony WF-C500': 115.00,  
                }

# Price range
price_range = input("Enter price range (e.g. 100-500): ").split("-")
price_min = float(price_range[0])
price_max = float(price_range[1])

# Brand
brand_choices = ["Sony", "Apple", "Bose", "Logitech", "Bowers & Wilkins", "Sennheiser", "Belkin", "Anker", "Edifier",
                  "Samsung", "Beats", "Jabra", "EPOS", "Nothing", "Bang & Olufsen"]
brand = input("Enter brand (" + ", ".join(brand_choices) + "): ")

# Functions
functions_choices = ["Noise Cancelling", "Ambient Sound", "Low Latency"]
functions = input("Enter functions (" + ", ".join(functions_choices) + "): ").split(",")
functions = [f.strip() for f in functions]

# Support Codec
codec_choices = ["AAC", "SBC", "LDAC"]
codec = input("Enter support codec (" + ", ".join(codec_choices) + "): ")

# App support
app_support_choices = ["Yes", "No", "Both"]
app_support = input("Enter app support (" + ", ".join(app_support_choices) + "): ")

# Battery Life
battery_choices = ["Less than 5 hours", "5-10 hours", "10-20 hours", "More than 20 hours"]
battery = input("Enter battery life (" + ", ".join(battery_choices) + "): ")

# Bluetooth Ver.
bluetooth_choices = ["5.0 or above", "5.2 or above", "6.0 or above"]
bluetooth = input("Enter Bluetooth version (" + ", ".join(bluetooth

# Initialize list of recommendations
    recommendations = []

    # Loop through headphones and earbuds dictionaries to find matches
    for product_dict in [headphone_dict, earbud_dict]:
        for product, price in product_dict.items():
            # Filter by price range
            if price >= price_min and price <= price_max:
                # Filter by brand
                if brand.lower() in product.lower():
                    # Filter by functions
                    if all(f.lower() in product.lower() for f in functions):
                        # Filter by codec support
                        if ('AAC' in codec and 'AAC' in product_dict[product].get('codec', '')) or \
                                ('SBC' in codec and 'SBC' in product_dict[product].get('codec', '')) or \
                                ('LDAC' in codec and 'LDAC' in product_dict[product].get('codec', '')):
                            recommendations.append(product)

    return recommendations
    
    # Headphone/Earbuds Recommendation Program

headphone_dict = {
    'Sony WH-1000XM5': 595.00,  
    'Apple Airpods Max': 999.00,  
    'Sony WH-1000XM4': 414.00,  
    'Bose Noise Cancelling Headphones 700': 699.95,  
    'Logitech G435 LIGHTSPEED Wireless': 249.90,  
    'Bowers & Wilkins Px7 S2 Headphones': 649.00,  
    'Sennheiser Momentum 4 Wireless': 599.95,  
    'Belkin Soundform Mini': 59.99,  
    'Anker SoundCore Life Q30': 241.95,  
    'Edifier W820NB': 168.00  
}

earbud_dict = {
    'Samsung Galaxy Buds 2': 279.00,  
    'Apple Airpods Pro (Gen 2)': 479.00,  
    'Beats Fit Pro': 349.95,  
    'Sony WF-1000XM4': 369.00,  
    'Jabra Elite 7 Active': 284.00,  
    'Jabra Elite 7 Pro': 296.00,  
    'EPOS GTW 270 Hybrid': 239.00,  
    'Nothing Ear 1': 189.00,  
    'Sennheiser Momentum TW 3': 378.00,  
    'Earfun Air Pro 3': 139.00,  
    'Bang & Olufsen Beoplay EX': 775.00,  
    'Jabra Elite 85t': 199.95,  
    'Sony WF-C500': 115.00  
}

# Price range
price_range = input("Enter price range (e.g. 100-500): ").split("-")
price_min = float(price_range[0])
price_max = float(price_range[1])

# Brand
brand_choices = ["Sony", "Apple", "Bose", "Logitech", "Bowers & Wilkins", "Sennheiser"]
print("Choose a brand from the following: ")
for i, brand in enumerate(brand_choices):
    print(f"{i+1}. {brand}")
brand_choice = int(input("Enter your choice: "))
brand = brand_choices[brand_choice-1]

# Functions
functions_choices = ["Noise Cancelling", "Ambient sound"]
print("Select functions you want from the following: ")
for i, function in enumerate(functions_choices):
    print(f"{i+1}. {function}")
functions_choice = int(input("Enter your choice: "))
functions = functions_choices[functions_choice-1]

# Codec support
codec_choices = ["AAC", "SBC", "LDAC"]
print("Select codec support you want from the following: ")
for i, codec in enumerate(codec_choices):
    print(f"{i+1}. {codec}")
codec_choice = int(input("Enter your choice: "))
codec = codec_choices[codec_choice-1]

# App support
app_choices = ["Y", "N", "Both"]
print("Select app support you want from the following: ")
for i, app in enumerate(app_choices):
    print(f"{i+1}. {app}")
app_choice = int(input("Enter your choice: "))
app = app_choices[app_choice-1]

# Battery life
battery_life_choices = ["<5 hours", "5-10 hours", "10-20 hours", ">20 hours"]
print("Select battery life you want from the following: ")

'''  # previous codes
