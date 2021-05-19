# import random


# # Create a function called get_random_temp().
# # This function should return an integer between -10 and 40 degrees (Celsius), selected at round(random.
# # Test your function to make sure it generates expected results.

# def get_random_temp(season):
#     if season == "winter":
#         return round(random.uniform(-10,9),1)
#     elif season == "Summer":
#         return round(random.uniform(30,40), 1)
#     elif season == "Spring":
#         return round(random.uniform(10,19),1)
#     elif season == "Autum":
#         return round(random.uniform(20,19),1)
#     elif season == "Winter":
#         return round(random.uniform(-10,1),10)
    


# # Create a function called main().
# # Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# # Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”


# # Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# # below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# # between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# # between 16 and 23
# # between 24 and 32
# # between 32 and 40

# # Change the get_random_temp() function:
# # Add a parameter to the function, named ‘season’.
# # Inside the function, instead of simply generating a round(random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# # Now that we’ve changed get_random_temp(), let’s change the main() function:
# # Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# # Use the season as an argument when calling get_random_temp().

# def main():
#     season = input("Whats the season? ")
#     temp = get_random_temp(season)
#     print(f"The current temperature is {temp} degrees Celsius.")
#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0<temp <16:
#         print('Quite chilly! Don’t forget your coat')
#     elif 16<temp <23:
#         print('Might not need your coat')
#     elif 23<temp <32:
#         print('T-Shirt weather')
#     elif 32<temp <40:
#         print('Not worth leaving the house')

# main()

    

