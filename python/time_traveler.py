def time_traveler(year):
    if year < 1900:
        print("Welcome to the future!")

    elif year >= 1900 and year <= 2020:
        print("Welcome to our year!")

    else:
        print("Welcome to the past.")

time_traveler(1850)
time_traveler(1900)
time_traveler(1950)
time_traveler(2020)
time_traveler(2100)
