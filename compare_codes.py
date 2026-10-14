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
    
    if len(guess) > 4 or len(guess) < 4:
        print("Ensure you have chosen for colours")

    #Handle different colour cases

    for colour in mutable_guess:
        count = 0
        if colour in mutable_colour_options:
            count +=1
    
    if colour in mutable_colour_options:
        if colour not in mutable_actual_code:
            count += 1
        print(f"{count} out of your 4 colour code options is incorrrect")
        return False

    if count == 3:
        print("So close! Only one value is incorrect")
        return False
    elif count == 2:
        print("You only got half of the colours correct")
        return False
    elif count == 1:
        print("You only got 1 out of 4 colours correct")
        return False
    else:
        print(f"One or more colours are not in the options: {colour_options}")
        return False

    

    

    
    
#     code_copy = list(actual_code)
#     for colour in guess:
#         colour = colour.lower()
        
#     if sorted(guess) == sorted(actual_code):
#         print("The codes are the same")

#     mutable_guess = guess
#     guess_list = list(mutable_guess)

#     print(mutable_guess)

code_comparison(("red", "Green"))
    