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
    'Sony WH-1000XM5': {'brand': 'Sony', 'price': 595.00, 'functions': 'Active Noise Cancelling, Ambient Sound, ',
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

brand_list = ["Anker", "Apple", "Bang & Olufsen", "Beats", "Belkin", "Bose", "Bowers & Wilkins", "Edifier", "EPOS",
              "Jabra", "Logitech", "Nothing", "Samsung", "Sennheiser", "Sony", "N/A"]

functions_list = ["Active Noise Cancelling", "Ambient Sound", "Auto Pause/Play", "Low Latency",
                  "Passive Noise Cancelling", "Quick Charge", "Voice Call", "Water Resistence", "Wireless Charging",
                  "N/A"]

codec_list = ["AAC", "aptX", "aptX Low Latency", "aptX Adaptive", "aptX HD", "LC3", "LDAC", "LHDC", "SBC", "N/A"]

app_support_list = ["Yes", "No", "N/A"]

battery_list = ["Less than 5 hours", "5-10 hours", "10-20 hours", "More than 20 hours", "N/A"]

'''
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
            return
        elif category_choice.lower() == "earbud":
            chosen_dict = earbud_dict
            return
        elif category_choice.lower() == "both":
            chosen_dict = headphone_dict | earbud_dict
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
                else:
                    n = 1
        return
    except ValueError:
        print("Invalid choice!")
        price_range_fc()


# Brand - brand of product
def brand_fc():
    try:
        print("Choose a brand from the following: ")
        for i, brand in enumerate(brand_list):
            print(f"{i + 1}. {brand}")
        brand_choice = int(input("Enter your choice (e.g. 16): "))
        if brand_choice <= 0 or brand_choice > 16:
            print("Invalid choice!")
            brand_fc()
        else:
            return brand == brand_list[brand_choice - 1]
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
    try:
        print("Choose a function from the following: ")
        for i, functions in enumerate(functions_list):
            print(f"{i + 1}. {functions}")
        functions_choice = int(input("Enter your choice (e.g. 10): "))
        if functions_choice <= 0 or functions_choice > 10:
            print("Invalid choice!")
            functions_fc()
        else:
            return functions == functions_list[functions_choice - 1]
    except ValueError:
        print("Invalid choice!")
        functions_fc()


# Support Codec - codec of product supported
def codec_fc():
    global codec
    try:
        print("Choose a codec from the following: ")
        for i, codecs in enumerate(codec_list):
            print(f"{i + 1}. {codecs}")
        codec_choice = int(input("Enter your choice (e.g. 10): "))
        if codec_choice <= 0 or codec_choice > 10:
            print("Invalid choice!")
            codec_fc()
        else:
            return codec == codec_list[codec_choice - 1]
    except ValueError:
        print("Invalid choice!")
        codec_fc()


# App support - choice on having app support or not
def app_support_fc():
    global app_support
    try:
        print("Would you like the headphone/earbud to include app support?")
        for i, app_support in enumerate(app_support_list):
            print(f"{i + 1}. {app_support}")
        app_support_choice = int(input("Enter your choice (e.g. 1): "))
        if app_support_choice <= 0 or app_support_choice > 3:
            print("Invalid choice!")
            app_support_fc()
        else:
            return app_support == app_support_list[app_support_choice - 1]
    except ValueError:
        print("Invalid choice!")
        app_support_fc()


# Battery Life - Battery life-long in hrs
def battery_life_fc():
    global battery
    try:
        print("Please choose battery life long (in Hrs): ")
        for i, battery in enumerate(battery_list):
            print(f"{i + 1}. {battery}")
        battery_choice = int(input("Enter your choice (e.g. 1): "))
        if battery_choice <= 0 or battery_choice > 5:
            print("Invalid choice!")
            battery_life_fc()
        else:
            return battery == battery_list[battery_choice - 1]
    except ValueError:
        print("Invalid choice!")
        battery_life_fc()


# Speciality - Special or Honours E.g. Best value
'''def speciality_fc():
    global speciality
    speciality_choices = ["Value", "Cheapest", "Pricey", "Long Usage Hours", "Good Sounding (in price range)",
                          "Best ANC", "Best Ambient", "Best Overall"]
    return speciality == input("Enter speciality (" + ", ".join(speciality_choices) + "): ")'''


# Recommend product to user by filtering preferences
def recommendation():
    # Get user preferences, call previous functions
    category_fc()
    price_range_fc()
    brand_fc()
    functions_fc()
    codec_fc()
    app_support_fc()
    battery_life_fc()
    # speciality_fc()

    # Filter products based on user choices
    filtered_products = []
    for key, product_info in chosen_dict.items():
        if (price_min <= product_info['price'] <= price_max) or (price_min == 0.00 and price_max == 0.00) and (
                brand in product_info['brand']) or (brand == "N/A"):
            if (functions in product_info['speciality']) or (functions == "N/A"):
                if (codec in product_info['speciality']) or (codec == "N/A"):
                    if (app_support == "N/A") or ((app_support == "iOS" and product_info['brand'] == "Apple") or (
                            app_support == "Android" and product_info['brand'] != "Apple")):
                        if (battery == "N/A") or (
                                "battery" in product_info['speciality'] and battery.lower() in product_info[
                            'speciality']):
                            filtered_products.append(key)
    print(filtered_products)


'''    
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

recommendation()  # price_min, price_max, brand, functions, codec
