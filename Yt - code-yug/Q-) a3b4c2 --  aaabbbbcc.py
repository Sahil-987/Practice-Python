input_ = 'a3b2c6e5d1f5'


# my method
pt1 = 0
pt2 = 1
result = ""
for i in range(len(input_)-int(len(input_)/2)):
    print(input_[pt1],input_[pt2])
    result += input_[pt1]*int(input_[pt2])
    pt1 += 2
    pt2 += 2

print(result)




# code-yt Yt
output = ""
for i in input_:
    if i.isalpha():
        var = i
    else:
        num = int(i)
        output += var*num
print(output)
        