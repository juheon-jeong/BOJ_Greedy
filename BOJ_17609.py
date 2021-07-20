def similar(a,left, right):
    while (left < right):
        if (a[left] == a[right]):
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrome(a, left, right):
    while (left < right):
        if (a[left] == a[right]):
            left += 1
            right -= 1
        else:
            tmp1 = similar(a, left+1, right)
            tmp2 = similar(a, left, right - 1)
            if (tmp1 or tmp2):
                return 1
            else:
                return 2
    return 0

testcase = int(input())

for i in range(testcase):
     a = input()
     result = palindrome(a, 0, len(a) - 1)
     print(result)