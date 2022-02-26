# # метод 1
# def get_summ(one, two, delimiter='&'):
#     summ =(f'{one} {delimiter} {two}'.upper())
#     print(summ)
# get_summ ('Learn','Python')

# # функция, которая вычисляет сумму квадратов двух переданных чисел
# def summ_square (a, b):
#     summ =(a**2)+(b**2)
#     print(summ)
# summ_square (3, 5)

# # метод 2
# def get_summ(one, two, delimiter='&'):
#     return(f'{one} {delimiter} {two}'.upper())
# result = get_summ ('Learn','Python')
# print(result)

# # функция, которая вычисляет сумму квадратов двух переданных чисел
# def summ_square (a, b):
#     return(a**2)+(b**2)
# result =summ_square (3, 5)
# print(result)

# функция, которая рассчитывает, сколько человек
# получит на руки денег с зарплаты. 
# В функцию передается сумма заработка. Например 
# если мы передадим в функцию 100, нам возвращается 87.
# И потом написать функцию которая рассчитывает годовой доход, 
# с использованием предыдущей функции
    
def tiped_salary(salary):
    tip_salary = salary - salary*13/100
    return(tip_salary)
month_cash=(tiped_salary(100000))
print (month_cash)

def annual_salary(resume):
    resume = month_cash*12
    return(resume)
year_cash=(annual_salary(month_cash))
print(year_cash)
