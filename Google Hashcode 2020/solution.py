import os
import csv
fileslist = []
for file in os.listdir("./"):
    if file.endswith(".in"):
        fileslist.append(file)
Score = 0
for fl in fileslist:
    
    lists = []
    with open(fl, newline = '\n') as data:
        data_reader = csv.reader(data, delimiter=" ")
        for line in data_reader:
            lists.append(line)
        
    ms = lists[0][0] # max number of slice we can have
    ms = int(ms)

    tp = lists[0][1] #total number of pizza we can have
    tp = int(tp)

    w = lists[1]
    

    #changing string in w to integer
    for i in range(len(w)):
        w[i] = int(w[i])    


    ind = list()
    lind = list()
    los = list()

    for j in range(len(w)):
        s =0
        ind = []
        #print(j)
        for i in range(len(w)-1-j,-1,-1):
            #print(i)
            s += w[i]

            if s < ms:
                ind.append(i)
                continue
    
            elif s == ms:
                ind.append(i)
                break
        
            elif s > ms:
                s -= w[i]
        #print()        
        los.append(s)        
        lind.append(ind)       
        
    

    oss = max(los) # it the total number of slice we wil order
    

    d = los.index(oss)# index of max number of slice
    

    e =lind[d] #e is final indexes for slices
    e.sort()
    
    with open(os.path.splitext(fl)[0]+".out", 'w+') as the_file:
        the_file.write(str(len(e)))
        the_file.write("\n")
        for val in e:
            the_file.write(str(val))
            the_file.write(" ")