#create a tuple with different data types 
tuplex = ("tuple" , False, 3.2 , 1 )
print(tuplex)


#create a tuple 
tuplex = ( 4, 6, 2, 8, 3, 1)
print(tuplex)


#tuples are immutable , so you cannot add new elements 
#using merge of tuples with the + operator  you can add an element and it will create a new tuple 

tuplex = tuplex + (9,)
print(tuplex)


#counts the number of occurences of item 50 from a tuple 
tuple = (50 , 60, 20 , 70 ,50 , 20 , 10)
print(tuple.count(50))


#create a tuple 
tuplex = (2, 4, 3, 5, 4, 6, 7,  8, 6, 1)
#used tuple [start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#its exclusive 
print(_slice)


#if the start index isnt defined , is taken from the beginning of the tuple 

_slice = tuplex[:6]
print(_slice)




