def Josephus_survive(list_people, step):
    step = step-1
    index = step
    while (len(list_people) > 1):

        print(list_people.pop(index))
        index = (index + step ) % len(list_people)
    return list_people.pop()



if __name__ == "__main__":
    result = Josephus_survive([1,2,3,4,5,6,7],3)
    print ("Result is: ",result)




