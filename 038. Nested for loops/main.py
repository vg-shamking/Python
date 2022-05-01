for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("-------------------")
#Position is important:
#print("-------------------") - once in the end
    #print("-------------------") - every finished i-line
        #print("-------------------") - every finished j-line