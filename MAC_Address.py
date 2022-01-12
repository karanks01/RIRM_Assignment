Str = input("Enter the String : ")

MAC = ':'.join([Str[i : i + 2] for i in range(0, len(Str), 2)])   
print(MAC.upper())

Str_Element = list(Str)

Total_Element = int(input("Total Number of element in mapper :  "))
mapper = {}

for i in range (Total_Element):
    key=input("Enter key :")
    value=input("Enter values :")
    mapper.update({key: value})
print(mapper)

convert = []
for item in Str_Element:
    convert.append(mapper.get(item,item))
    " ".join(convert)
new = ''.join(convert)

Updated_MAC = ':'.join([new[i : i + 2] for i in range(0, len(new), 2)])
print(Updated_MAC.upper())
