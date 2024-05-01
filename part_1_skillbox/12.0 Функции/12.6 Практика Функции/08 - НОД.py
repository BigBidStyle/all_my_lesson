# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

def nod(a, b):
  if a > b:
      temp = b
  else:
      temp = a
  for i in range(1, temp + 1):
      if (a % i == 0) and (b % i == 0):
          nod = i
  return nod

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

print('НОД: ', nod(num_1, num_2))