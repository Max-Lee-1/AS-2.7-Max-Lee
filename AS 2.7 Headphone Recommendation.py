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

# headphone_dict[1] =

print(headphone_dict)
print('\n')
print(earbud_dict)

