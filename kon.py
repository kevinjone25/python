str = 'label'

convert_str = ' '.join(format(ord(i),'b')for i in str)

str_split = convert_str.split(' ')
# print(str_split)
num = bin(13)


for i in str_split:
    i += '0b'

l = []
for i in str_split:
    l.append(int(i,2)^0b1101)

print(l)

for i in l:
    print(chr(i))


