def get_values():
    try:
        x, y = map(int, input().split())
        return x, y

    except ValueError as error :
        print(error)
        return 0, 0
    finally:
        print('Блок finally выполнился до return')

x , y = get_values()
print(x, y)