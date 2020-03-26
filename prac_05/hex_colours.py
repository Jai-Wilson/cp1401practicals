


COLOUR_CODE = {"aliceblue": "f0f8ff", "antiquewhite": "faebd7", "aquamarine1": "7fffd4", "azure1": "f0ffff",
               "beige": "f5f5dc", "darkgreen": "006400", "ghostwhite": "f8f8ff", "indianred": "cd5c5c",
               "lightblue": "add8e6", "violet": "ee82ee"}

print(COLOUR_CODE)

user_code = input("What is the colour you would like the code of? ")
while user_code != "":
    if user_code in COLOUR_CODE:
        print(user_code, "is", COLOUR_CODE[user_code])
    else:
        print("Invalid input")
    user_code = input("What is the colour you woudl like the code of?")


