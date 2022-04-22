

finalList= {'turtle':['turtle10']}

keyList = ['turtle','cat','mouse','dog']
valueList =['turtle1','turtle2','turtle1','cat1','cat2','dog','dog1']
for i in keyList:
        finalList[i]= []

for items in finalList.keys():
    #print('***Keys***'+items)
    for elements in valueList:
        #print('***Values***'+elements)
        res = not any(finalList.values())
        if items in elements:
                
            if elements not in finalList[items]:
                finalList[items].append(elements)

                
for key, value in finalList.items():
    for i in value:
        print(key,' : ', i)
            

        

print(finalList)
#finalList[items].append(elements)
#print('VALUE LIST: '+valueList.values())