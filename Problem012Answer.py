def isHappy(n):
        arr = [n]  # Store the initial number in a list
        result = [int(digit) for digit in str(arr[0])]  # Split the number into its digits
        result_2 = 0  # This will hold the sum of the squares of the digits
        i = 0  # Counter for the number of iterations
        n_len = len(result)  # Number of digits in the current number
        while i < 10:  # Limit the number of iterations to avoid infinite loops
            j = 0  # Index for iterating through digits
            while j < (n_len):  # Loop through each digit
                result_2 += result[j]**2  # Add the square of the digit to result_2
                j+=1
            if result_2 == 1:  # If the sum of squares is 1, it's a happy number
                return True
            else:
                i +=1  # Increment the iteration counter
                new_arr = [result_2]  # Prepare the new number for the next iteration
                result = [int(digit) for digit in str(new_arr[0])]  # Split new number into digits
                result_2 = 0  # Reset the sum for the next iteration
                n_len = len(result)  # Update the number of digits
        return False  # If 1 is not reached in 10 iterations, assume not happy
    
y = 1111111  # Example number to check
ans = isHappy(y)  # Call the function and store the result
print(ans)  # Print whether the number is happy or not
