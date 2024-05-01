# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# for i_elem in range(2, 8):
#         print(nums[i_elem], end=" ")
#
# print()
# for i_elem in range(2, 8):
#         print(new_nums[i_elem], end=" ")

# -----------------------

nums = [x for x in range(1, 101) if x % 10 == 0]
new_nums = nums[:]
new_nums[3] = 0

print(f"{new_nums[2:5]} - От двойки до пятерки")
print(f"{new_nums[5:]} - От начала и до пятерки")
print(f"{new_nums[5:]} - От пятерки и до конца списка")
print(f"{new_nums[2:8:2]} - От двух до восьми с шагом два")
print(f"{new_nums[::-1]} - От конца в начало с шагом один")
new_nums[:3] = [1, 1, 1]
print(f"{new_nums}- Первые три индекса равны 1")
new_nums[:3] = [1]
