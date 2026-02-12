def isHappy(n):
        arr = [n]
        result = [int(digit) for digit in str(arr[0])]
        result_2 = 0
        i = 0
        n_len = len(result)
        while i < 10:
            j = 0
            while j < (n_len):
                result_2 += result[j]**2
                j+=1
            if result_2 == 1:
                return True
            else:
                i +=1
                new_arr = [result_2]
                result = [int(digit) for digit in str(new_arr[0])]
                result_2 = 0
                n_len = len(result)
        return False
    
y = 1111111
ans=isHappy(y)
print(ans)