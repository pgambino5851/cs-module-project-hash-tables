def divBy3(arr):
    res = []
    for i in range(0, len(arr)):
        if arr[i] % 3 == 0:
            res.append(arr[i])
    return res

testArr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
print(divBy3(testArr))