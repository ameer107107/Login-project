s = int(input('Enter  num. of list : '))

for i in range(0,s):
    x = str(input('Enter  name : '))
    ls.append(x)


for i in range  (0, len(ls)):
     if ls[len(i)] > 4 :
            ls_more_four_chr.append(ls[i])
     else :
            ls_four_chr.append(ls[i])

print(ls_four_chr)
print(ls_more_four_chr)