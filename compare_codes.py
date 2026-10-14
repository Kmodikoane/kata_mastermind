def code_comparison(guess):
    """
    This program guesses the secret code comprising of 4 colours
    Parameters: guess -> list of 4 colours
    Returns : True or False -> Bool

    """
    colour_options =["red", "navy","pink", "white", "ginger", "green"]
    actual_code = ("red", "green", "pink", "white")

    if sorted(guess) == sorted(actual_code):
        print("You guessed the code correctly")
    
#     code_copy = list(actual_code)
#     for colour in guess:
#         colour = colour.lower()
        
#     if sorted(guess) == sorted(actual_code):
#         print("The codes are the same")

#     mutable_guess = guess
#     guess_list = list(mutable_guess)

#     print(mutable_guess)

code_comparison(("red", "green", "pink", "white"))
    