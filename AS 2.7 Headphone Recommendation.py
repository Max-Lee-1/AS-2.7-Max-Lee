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
                              Rating (added form reference): the best overall, Best in audio, best in user-friendly...
'''
headphone_dict = {'Sony WH-1000XM5': 1,  # best all rounded, best ANC, comfortable
                  'Apple Airpods Max': 2,  # best iphone, most expensive, 2nd best for workout
                  'Sony WH-1000XM4': 3,  # best sounding bass, best for workout, Best Bluetooth codec support
                  'Bose Noise Cancelling Headphones 700': 4,  # best phone call
                  'Focal Bathys': 6,  # best sounding (over-ear)
                  'Logitech G535 LIGHTSPEED Wireless': 7,  # best budget gaming
                  'Bowers & Wilkins Px7 S2 Headphones': 8,  # best look, most comfort, 3rd best Bluetooth codec support
                  'Sennheiser Momentum 4 Wireless': 9,  # 2nd best sounding bass, 2nd best Bluetooth codec support
                  'Belkin Soundform Mini': 10,  # best for kids
                  'Audio-Technica ATH-M20xBT': 11,  # best cheapest
                  'Anker SoundCore Life Q30': 12,  # best value
                  'Edifier W820NB': 13,  # best sounding cheapest
                  }

earbud_dict = {'Samsung Galaxy Buds 2': 1,  # best all rounded
               'Apple Airpods Pro (Gen 2)': 2,  # best iphone, best sounding upper-mid range price, most expensive
               'Beats Fit Pro': 3,  # best workout
               'Sony WF-1000XM4': 4,  # best ANC (Active Noise Cancelling), 2nd best Bluetooth codec support
               'Jabra Elite 7 Active': 5,  # best versatility
               'Jabra Elite 7 Pro': 6,  # best sounding in lower-mid range price
               'EPOS GTW 270 Hybrid': 7,  # best gaming
               'Nothing Ear 1': 8,  # best looking
               'Sennheiser Momentum TW 3': 9,  # best sounding bass
               'Earfun Air Pro': 10,  # good-looking, all rounded in cheap price range
               '1MORE PistonbBuds Pro': 11,  # best cheapest with all rounded feature
               'Bang & Olufsen Beoplay EX': 12,  # Expensive, great-looking, nice sound
               'Jabra Elite 85t': 13,  # best Bluetooth codec support
               'OnePlus Nord Buds': 14,  # best value
               'Sony WF-C500': 15,  # best sounding cheapest
                }

