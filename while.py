# def cut_cake(people):
#     try:
#         z = 1 / people
#         print(f'Каждый получит {z} пирога')
#     except (ZeroDivisionError, TypeError):
#         print("Не могу поделить")
# cut_cake (11)

# # while True:
# #     user_say = input('Скажи что-нибудь: ')
# #     if user_say == 'Пока':
# #         print('Ну пока')
# #         break
# #     else:
# #         print('Сам ты {}'.format(user_say))

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}

names = ['Оля', 'Петя', 'Вася', 'Маша']

for student in is_male:
    for pers in names:
        if is_male[0] ==names[0]:
            print(f'Женский')


# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# # ???