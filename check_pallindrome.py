string = "12344321"

isPallindrome = False

for i in range(0, len(string)):
    print(f"{string[i]}")
    for j in reversed(range(0 ,len(string))):
        print(f"{string[i]} and {string[j]}")
        if  string[i] == string[j]:
            isPallindrome = True
        else:
            isPallindrome = False
print(isPallindrome)