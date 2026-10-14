def code_comparison(guess):
    """
    This program guesses the secret code comprising of 4 colours
    Parameters: guess -> tuple of 4 colours
    Returns : True or False -> Bool

    """
    colour_options =("red", "navy","pink", "white", "ginger", "green")
    actual_code = ("red", "green", "pink", "white")

    mutable_actual_code  = list(actual_code)
    mutable_guess = list(guess)
    mutable_colour_options = list(colour_options)

    code = []
    for word in mutable_guess:
        code.append(word.lower())

    guess_tuple_lower = tuple(code)


    if guess_tuple_lower == actual_code:
        print("You guessed the code correctly!")
        return True

    

    
    
#     code_copy = list(actual_code)
#     for colour in guess:
#         colour = colour.lower()
        
#     if sorted(guess) == sorted(actual_code):
#         print("The codes are the same")

#     mutable_guess = guess
#     guess_list = list(mutable_guess)

#     print(mutable_guess)

code_comparison(("red", "Green", "PINK", "whITe"))
    