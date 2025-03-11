a = 100
b = "this is a test"
c = 1.0
d = True
e = None


print(hash(a), hash(b), hash(c), hash(d), hash(e))


# input hashable  stirng int bool float      tuple 裡面的值也要是hashable
# not input hash value list dict set

print(hash("Hello"))
print("Doing other stuff..")
for i in range(10): 
    pass
print(hash("Hello"))


print(hash("Look at me!"))  #reverse engineering
print(hash("Look at me!!"))
print(hash("Look at me!!!"))