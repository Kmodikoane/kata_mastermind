def code_comparison(guess):
    """
    This program guesses the secret code comprising of 4 colours
    Parameters: guess -> tuple of 4 colours
    Returns : True or False -> Bool

    """
    
    colour_options =("red", "navy","pink", "white", "ginger", "green")
    actual_code = ("red", "green", "pink", "white")

    if guess == actual_code:
        return True

    mutable_actual_code  = list(actual_code)
    mutable_guess = list(guess)
    mutable_colour_options = list(colour_options)

    #Consider capitalisation of tuple
    code = []
    for word in mutable_guess:
        code.append(word.lower())

    guess_tuple_lower = tuple(code)

    if guess_tuple_lower == actual_code:
        print("You guessed the code correctly!")
        return True

    #Handle different colour cases
    count = 0
    for colour in mutable_colour_options:
        if colour in mutable_actual_code:
            count +=1
            if count == 4:
                return True
            elif count == 3:
                print("So close! One color is incorrect")
                return False
            elif count == 2:
                print("You only have 2 colour correct")
                return False
            elif count == 1:
                print("You only got 1 out 4 color correct")
                return False
            else:
                return False
        else:
            return False

    

    

    
    
#     code_copy = list(actual_code)
#     for colour in guess:
#         colour = colour.lower()
        
#     if sorted(guess) == sorted(actual_code):
#         print("The codes are the same")

#     mutable_guess = guess
#     guess_list = list(mutable_guess)

#     print(mutable_guess)

code_comparison(("red", "Green", "PINK", "whITe"))
    