s = 'my name is solomia' # immutable

print(len(s))

# 1 - indexes
# s[0] = 'M' ERROR
print(s[3])
print(s[-5])

# 2 - slices
print(s[3:6])
print(s[3:10:2])
print(s[::-1])
s = 'M' + s[1:11] + s[11].upper() + s[12:]
#print(s)

# 3 - method
# s = s.replace('m', 'M')
# s = s.upper()
# s = s.title()
print(s)