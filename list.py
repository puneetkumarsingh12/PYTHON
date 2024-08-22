lw=[5,4]

print(len(lw))

lw.insert(0,-9)

print(lw)

lw.append(52)

print(lw)

lw.extend(lw)

print(lw)

lw.remove(5)

print(lw)

print(lw)

print()

# lw.clear()

print(lw)

print()

lw.sort()
print(lw)
print()
lw.sort(reverse=True)
print(lw) 
print()
lw.reverse()
print(lw)
print()
print(lw[::-1])
print()
l2=[[4,5,60],[8,9,7],[11,22,33]]
print(l2[2][2])