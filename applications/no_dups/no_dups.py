def no_dups(s):
    cache = {}
    arr = s.split()
    resArr = []
    for i in range(0, len(arr)):
        key = arr[i]
        # print(f"arr[i] is {key}")
        if arr[i] not in cache:
            # print(f"The cache is {cache} and arr[i] {arr[i]} is not in there")
            cache[key] = 1
            resArr.append(arr[i])
        else:
            continue
    # print(resArr)
    resStr = " "
    return resStr.join(resArr)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))