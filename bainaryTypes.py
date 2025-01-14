

HabluList  = [1,2,5,88,1,4,7,6,255]

b = bytes(HabluList)

print(b)

print(type(b))

B = bytearray(HabluList)

print(B)
print(type(B))

B[1] = 100

print(B[1])