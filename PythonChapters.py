x = 5 #KnpowTheDataTypesClassInt
print(type(x))
x = "Hello World" #DataTypeString
print(x)
print(type(x)) 
x = 20 #int
print(type(20))
x = 20.5 #float
print(type(x))
print(x)
x = 1j #complex
print(type(x))
print(x)
x = ["Apple","Cherry","Banana"] #list
print(type(x))
print(x)
x = ("Apple","Banana","Cherry") #tupple
print(type(x))
print(x)
x = range (6) #range
print(type(x))
print(x) #dict
x = {"name" : "John","Age" : 36}
print(type(x))
print(x) #set
x = {"Apple","Banana","Cherry"}
print(type(x))
print(x) #frozenset
x = frozenset({"Apple","Banana","Cherry"})
print(x)
x = True #bool
print(x)
x = b"Hello" #bytes
print(type(x))
x = bytearray(5) #bytearray
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = 1 #integer
y = 2.8 #float
z = 1j #complex
a = float(x)
b = int(y)
c = complex(z)
print(a)
print(b)
print(c)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)
a = "Hello World" #string
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' #multilinestring
print(a)
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free"in txt:
    print("Yes,'free' is present")
txt = "The best things in life are free!"
print("expensive" not in txt)
print("No,'expensive' is Not present")

