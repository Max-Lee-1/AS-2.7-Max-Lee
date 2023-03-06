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
                              Bluetooth Ver. (added from reference): 5.0 or above, 5.2 or above...
                              Speciality (added form reference): the best overall, Best in audio, best in user-friendly...
                              Info: Ship Y/N; Retail Y/N; Overall rating (May add other ratings);
'''
headphone_dict = {'Sony WH-1000XM5': 595.00,  # best all rounded, best ANC, comfortable
                  'Apple Airpods Max': 999.00,  # best iphone, 2nd most expensive, 2nd best for workout
                  'Sony WH-1000XM4': 414.00,  # best sounding bass, best for workout, Best Bluetooth codec support
                  'Bose Noise Cancelling Headphones 700': 699.95,  # best phone call
                  'Logitech G435 LIGHTSPEED Wireless': 249.90,  # best budget gaming
                  'Bowers & Wilkins Px7 S2 Headphones': 649.00,  # best look, most comfort, 3rd best Bluetooth codec support
                  'Sennheiser Momentum 4 Wireless': 599.95,  # 2nd best sounding bass, 2nd best Bluetooth codec support
                  'Belkin Soundform Mini': 59.99,  # best for kids
                  'Anker SoundCore Life Q30': 241.95,  # best value
                  'Edifier W820NB': 168.00,  # best sounding cheapest
                  }

earbud_dict = {'Samsung Galaxy Buds 2': 279.00,  # best all rounded
               'Apple Airpods Pro (Gen 2)': 479.00,  # best iphone, best sounding upper-mid range price, expensive
               'Beats Fit Pro': 349.95,  # best workout
               'Sony WF-1000XM4': 369.00,  # best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support
               'Jabra Elite 7 Active': 284.00,  # best versatility
               'Jabra Elite 7 Pro': 296.00,  # best sounding in lower-mid range price
               'EPOS GTW 270 Hybrid': 239.00,  # best gaming
               'Nothing Ear 1': 189.00,  # best looking
               'Sennheiser Momentum TW 3': 378.00,  # best sounding bass
               'Earfun Air Pro 3': 139.00,  # best value, good-looking, all rounded
               'Bang & Olufsen Beoplay EX': 775.00,  # Most expensive, great-looking, nice sound
               'Jabra Elite 85t': 199.95,  # best Bluetooth codec support
               'Sony WF-C500': 115.00,  # best sounding cheapest
                }

'''# Headphone/Earbuds Recommendation Program

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
'''


# Price range
price_range = input("Enter price range (e.g. 100-500): ").split("-")
price_min = float(price_range[0])
price_max = float(price_range[1])

# Brand
brand_choices = ["Anker", "Apple", "Bang & Olufsen", "Beats", "Belkin", "Bose", "Bowers & Wilkins", "Edifier", "EPOS",
                 "Jabra", "Logitech", "Nothing", "Samsung", "Sennheiser", "Sony"]
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
bluetooth = input("Enter Bluetooth version (" + ", ".join(bluetooth_choices) + "): ")


print(headphone_dict)
print('\n')
print(earbud_dict)
print(brand_choices)

