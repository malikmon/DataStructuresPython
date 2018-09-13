# Passing an empty dictionary
def words_to_int(text):
    # If dictionary is empty
    numwords = {}
    print ("REACHED !!!!!")
    # list to store units place
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
              "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # list to store tens place
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    # list to store scale
    scales = ["hundred", "thousand", "million"]

    numwords["and"] = (1, 0) # set is defined to store "and" word

    # to generate dictionary using dictionary
    for idx, word in enumerate(units):
        numwords[word] = (1,idx)
    for idx, word in enumerate(tens):
        numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):
        numwords[word] = (10 ** (idx * 3 or 2), 0)
    print(numwords)
    current = result = 0
    for word in text.split():
        if word not in numwords:
            raise Exception("Illegal words ", word)
        else:
            scale, increment = numwords[word]
            current = current * scale + increment
            print(current)
        if scale > 100:
            result = result + current
            current = 0
    return current + result

if __name__ == "__main__":
  number = words_to_int("five thousand four hundred")
  print("Number is", number)





































