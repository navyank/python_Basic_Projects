a=['navya',432,'iliyana','apple','apple',8.90,'kaapi']
b=['aby',123]
print(a+b)
print(a)#o/p=['navya', 432, 'iliyana', 'apple', 'apple', 8.9, 'kaapi', 'aby', 123]
a[0]='varsha'
print(a)#o/p=['varsha', 432, 'iliyana', 'apple', 'apple', 8.9, 'kaapi']
print(type(a))
s=tuple(a)
print(s)#o/p=('varsha', 432, 'iliyana', 'apple', 'apple', 8.9, 'kaapi')
print(type(s))
print(a)
w=list(s)
print(w)
print(s)
a[0]=123
print(a)
print(a[:])
print(a[2:5])
print(a[:-1])
print(b*2)


# list are the collection of data of different datatype enclosed in sqauare bracket.
# mutable(can be changed)
# values are accessed using indexing.(start from 0 end in -1)
# (+) and (*) operation are allowed.