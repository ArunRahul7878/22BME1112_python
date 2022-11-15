lst1 = []
lst2 = [10,12,15]
lst3 = [1,2,'hello','world',84,'blablabla']
lst4 = [['hello','world'],['!!!']]
print(lst1)

print(lst2[2])

print(lst3[2] , lst3[5])

print(lst4[0][0] , lst4[0][1] , lst4[1][0])

n_list = ['Happy',[3,0,1,4]]
print(n_list[1][2],n_list[1][3],n_list[1][0])

lst5 = list('programizzzzaaaa')
print(lst5[:])
print('i n s t a',lst5[3:7])


#append
lst3.append('ttskk')
print(lst3)

#copy
lst1 = lst5.copy()
print(lst1)

#clear
lst1.clear()
print(lst1)

#count
print(lst5.count('a'))

#insert
lst3.insert(3,'OMG')
print(lst3)

#extend
lst2.extend([1,2,3,4])
print(lst2)
