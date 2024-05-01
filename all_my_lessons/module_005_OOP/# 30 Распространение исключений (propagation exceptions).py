def function2():
    return 1 / 0

def function1():
    try:
        return function2()
    except:
        print('Func1_error')
print('Я к вам пишу - чего же боле?')
print('Что я могу еще сказать?')
print('Теперь, я знаю, в вашей воле')
function1()
print('Меня презреньем наказать.')
print('Но вы, к моей несчастной доле')
print('Хоть каплю жалости храня,')
print('Вы не оставите меня.')