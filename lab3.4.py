'Екі бүтін А және В саны берілген, A>B. А-дан В-ға дейінгі барлық '
'тақ сандарды кему ретімен басып шығарыңыз.'
'Бұл тапсырмада if операторынсыз орындай аласыз.'
'Даны два целых числа A и В, A>B. Выведите все нечётные'
'числа от A до B включительно, в порядке убывания.'
'В этой задаче можно обойтись без инструкции if.'


a = int(input("a: "))
b = int(input("b: "))
if (a<b):
    print("A > B boluy kerek!!!", end=" ")
else:
    for i in range(a, b-1, -1):
        if i % 2 != 0:
            print(i, end=" ")



