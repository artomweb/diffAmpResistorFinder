def convert_to_int(s):
    index_of_k = s.find('k')
    if index_of_k != -1:
        s = float(s.replace("k", "."))
        return int(s * 1000)

    index_of_M = s.find('M')
    if index_of_M != -1:
        s = float(s.replace("M", "."))
        return int(s * 1000)

    
    return int(s)

file_path = "resistorValues.txt"
values = []
with open(file_path, 'r') as file:
    for line in file:
        value = line.strip()
        values.append(convert_to_int(value))

# vout = 3.3
# shuntR = 0.025
# maxCurrent = 2
vout = 3.3
shuntR = 1.1
maxCurrent = .6

valToFind = vout / (maxCurrent * shuntR)


print(valToFind)

absErrors = []

for i in values:
    for j in values:
        thisRatio = i/j
        absError = thisRatio - valToFind
        # print(i, j, absError)
        absErrors.append([i,j,absError])


sorted_values = sorted(absErrors, key=lambda x: abs(x[2]))

# print(sorted_values)

for i in sorted_values[:10]:
    print(i)