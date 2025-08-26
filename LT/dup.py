my_list =[1,2,3,4,5,5,6,6]
seen = set()
duplicates =[]

for items in my_list :
    if items in seen :
        print("Duplicate Found!")
    else :
        seen.add(items)
    
