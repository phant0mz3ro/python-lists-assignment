a = [1,2,3]
b = a

b[0] = 100

print(a)
print(b)
print(id(a))
print(id(b))

"""
why did both lists change?
both a and b point to the object in memory so b changed the object that a also points to 
why are the ids the same?
because they both point to the same address
what does this mean?
variables don't hold data in the conventional sense, instead they point to the address in memory
"""