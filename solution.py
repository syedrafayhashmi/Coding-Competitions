import os
import csv

for file in os.listdir("./"):
    if file.endswith(".in"):
        fileslist.append(file)
Score = 0
for fl in fileslist:
    fileslist = []
    lists = []
    with open(fl, newline = '\n') as data:
        data_reader = csv.reader(data, delimiter=" ")
        for line in data_reader:
            lists.append(line)

    line1 = lists[0]

    line2 = lists[1]

    line2i = []
    for x in line2:
        line2i.append(int(x))
    
    line1i = []
    for x in line1:
        line1i.append(int(x))

    sumvaluelist = []
    type_of_pizza  = []

    for i in range(-1,-len(line2i)-1,-1):
    
        sumvalue = 0
        temp_type = []
        for x in line2i[i::-1]:
            sumvalue+=x
        
            if sumvalue == line1i[0]:
                temp_type.append(x)
            
                break
            if sumvalue > line1i[0]:
                sumvalue -= x
            
                continue
            if sumvalue < line1i[0]:
                temp_type.append(x)
            
                continue # for less than sum value
        type_of_pizza.append(temp_type)
        sumvaluelist.append(sumvalue)
    print(f"Score: {max(sumvaluelist)}")
    Score += max(sumvaluelist)
    index_final_type = sumvaluelist.index(max(sumvaluelist))
    selected_pizzas  = type_of_pizza[index_final_type][::-1] # for reversing
    wrtfile = [] 
    final_pizza_types =  0

    for pizza in selected_pizzas:
        wrtfile.append(str(line2i.index(pizza)))
    l1 = str(len(wrtfile))
    l2 = wrtfile 
    with open(os.path.splitext(fl)[0]+".out", 'w+') as the_file:
        the_file.write(l1)
        the_file.write("\n")
        for val in l2:
            the_file.write(str(val))
            the_file.write(" ")
print(f"Total Score: {Score}")