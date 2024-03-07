# In this function we have to check for all NULL values for each types
# I use the match case format to check certain types and for the NaN value,
# I'll check the case manually cuz of the non existant variable NaN
# With few research, we can deduced that a float variable is NaN by compare itself by itself, if it's different, then it's NaN
# NaN values are considered unequal to all other values, including themselves, that's why we can use that
def NULL_not_found(object: any) -> int:
    strBuffer = ""

    match(object):
        case None:
            strBuffer = "Nothing: "
        case False:
            strBuffer = "Fake: "
        case 0:
            strBuffer = "Zero: "
        case '':
            strBuffer = "Empty: "
        case _:
            if (type(object) == float and object != object):
                print("Cheese: " + str(object) + " " + str(type(object)))
                return 0
            
            print("Type not Found")
            return 1

    print(strBuffer + str(object) + (" " if (len(str(object)) > 0) else "") + str(type(object)))
    return 0
