ma= [['A','B','C'],['D','E','F'],['G','H','I']]
print(ma)

for x in ma:
    for e in x:
        print(e, end=" ")
print()
    
i = 0  
while i < len(ma):
    j = 0 
    while j < len(ma[0]):  
        print(ma[i][j], end=" ")
        j += 1
    i += 1