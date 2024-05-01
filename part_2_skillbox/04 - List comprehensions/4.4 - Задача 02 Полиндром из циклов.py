def is_palindrome(num_list):
    revers_list = num_list[::-1]
    if num_list == revers_list:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 3, 2]
answer = []

for i_nums in range(0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print(f"Исходный  список: {nums}")
print(f"Нужно чисел для полиндрома: {len(answer)}")
print(f"Список этих чисел: {answer}")
