#cameron mitchell
#2/11/21
#study support

#inizalize arrays

pupils = 0
pupils = int(input("Please input the amount of pupils: "))
pupilname = [""] * pupils
Noclass = [0] * size
test1 = [0.0] * pupils
test2 = [0.0] * pupils
average = [0.0] * size
day = [""] * size

#inputs

for index in range(pupils):

    #Getting pupil name
    name[index] = str(input("Please input pupil name: "))

    #Getting class number
    Noclass[index] = int(input("Please input class Number: "))

    #input valdition on class number
    while Noclass[index] <1 or Noclass[index] > 2:

        Noclass[index] = int(input("Please input a class either 1 or 2: "))

    #getting test 1 mark
    test1[index] = float(input("Please input test1 score: "))

    #input validation on mark
    while test1[index] < 0 or test1[index] > 20:
        test1[index] = float(input("Pleae input a score between 0 and 20: "))

    #Getting test mark 2
    test2[index] = float(input("Please input test1 score: "))

    #input validation on test mark 2
    while test2[index] < 0 or test2[index] > 20:
        test2[index] = float(input("Pleae input a score between 0 and 20: "))



    #calculations

    #setting average to test 1 + test 2 divided by 2 then rounded to 1 decimal place
    average[index] = round((test1[index] + test2[index]) / 2,1)

#END FOR

#selection

for index in range(pupils):

    #Checking whether Noclass is 1 and the average mark is above 15
    if Noclass[index] == 1 and average[index] >=15:
        #Setting revision day to Monday
        day[index] = "Monday"

    #Checking whether the day is 2 and greater than 15
    elif Noclass[index] == 2 and average[index] >=15:
        #setting revision to tuesday
        day[index] = "Tuesday"

    #else just set revision day to Wednesday
    else:
        day[index] = "Wednesday"

#END FOR

#output

for index in range(pupils):
    #Output name
    print(name[index])

    #output Nocalass
    print(Noclass[index])

    #output average mark
    print(average[index])

    #output revision day
    print(day[index])

    #create space
    print()

#END FOR