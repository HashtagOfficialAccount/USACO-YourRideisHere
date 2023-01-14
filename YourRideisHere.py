'''
LANG: PYTHON3
PROG: ride
'''


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def comet(comet):
    c_checker = 0
    index = 0
    comet = comet.upper()
    if True:
        comet_num = 1
        for i in comet:
            index = 1
            for k in letters:
                if i == k:
                    comet_num = comet_num * index
                    break
                else:
                    index += 1
        return comet_num % 47

def group(group):
    g_checker = 0
    index = 0
    group = group.upper()
    if True:
        group_num = 1
        for i in group:
            index = 1
            for k in letters:
                if i == k:
                    group_num = group_num * index
                    break
                else:
                    index += 1
        return group_num % 47
                                
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

cometName = fin.readline().strip()
groupName = fin.readline().strip()

cometNumber = comet(cometName)
groupNumber = comet(groupName)
if(cometNumber == groupNumber):
    fout.write("GO\n")    
else:
    fout.write("STAY\n")    
fout.close()        
