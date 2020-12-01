def isArmstrong(num : int) -> bool:
    temp :int = num
    sum :int = 0
    while temp:
        sum += ((temp % 10) ** 3)
        temp //= 10
    return (sum == num)

# MAIN #
num = int(input("Enter the number to check "))
print(num, end = " ")
print("is an Armstrong Number") if isArmstrong(num) else print("is NOT an Armstrong Number")