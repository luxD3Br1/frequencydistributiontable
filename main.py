

# data
dataTemp = [112, 100, 127, 120, 134, 118, 105, 110, 109, 112,
            110, 118, 117, 116, 118, 122, 114, 114, 105, 109,
            107, 112, 114, 115, 118, 117, 118, 122, 106, 110,
            116, 108, 110, 121, 113, 120, 119, 111, 104, 111,
            120, 113, 120, 117, 105, 110, 118, 112, 114, 114]

# number of data items
n = len(dataTemp)
# class interval
ci = 7
# Sorting from ascending (lowest to highest)
dataTemp.sort()

#  getting range
range = dataTemp[-1] - dataTemp[0]

# determining the class size
classSize = round(range/ci)

# class interval lower limit
lower = []
a = dataTemp[0]
b = 0
while b < ci:
    lower.append(a)
    a += 5
    b += 1
# class interval upper limit
upper = []
a = (dataTemp[0] + 5) - 1
b = 0
while b < ci:
    upper.append(a)
    a += 5
    b += 1
# class interval Lower Boundary
lb = []
a = dataTemp[0]  - 0.5
b = 0
while b < ci:
    lb.append(a)
    a += 5
    b += 1

# class interval upper bounday
ub = []
a = (dataTemp[0] + 5.5) - 1
b = 0
while b < ci:
    ub.append(a)
    a += 5
    b += 1

# class mark
cMark = []
i = 0
while i < len(upper):
    cMark.append((upper[i]+lower[i])/2)
    i += 1

# frequency
fMark = []
i = 0
count = 0
while i < len(upper):
    for x in dataTemp:
        if upper[i] >= x and x >= lower[i] :
            count += 1
    fMark.append(count)
    count = 0
    i += 1
# less than cumulative frequency
lcf = []
lc = 0
for x in fMark:
    lc += x
    lcf.append(lc)
# Greater than cumulative frequency
gcf = []
gc = 0
for x in reversed(fMark):
    gc += x
    gcf.append(gc)

# relative frequency
rf = []
r = 0
for x in fMark:
    rf.append(str(round((x/50)*100)) + "%")
# ------------------------------------------------------------------------------
cntr =0
print("Data:")
for x in dataTemp:
    cntr += 1
    print(x, end=" ")
    if cntr % 10 == 0:
        print("\n")
# ------------------------------------------------------------------------------
print(
      " Num of Data: {} \n "
      "Range: {} \n "
      "ClassSize: {} \n "
      "Class Interval Lower Limit: {} \n "
      "Class Interval Upper Limit: {} \n "
      "Lower Boundary: {} \n "
      "Upper Boundary: {} \n "
      "Class Mark: {} \n "
      "Frequency: {} \n "
      "Less than cumulative frequency: {} \n "
      "Greater than cumulative frequency: {} \n "
      "Relative Frequency: {} \n".format(n, range, classSize, lower, upper, lb, ub, cMark, fMark, lcf, gcf, rf))
