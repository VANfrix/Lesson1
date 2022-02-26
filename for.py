# for number in range(5):
#     print(f'Номер {number}')

# for letter in 'python':
#     print(letter.upper())

# my_string = 'Привет,  я учу Python'

# for word in my_string.split():
#     print(f'Длина слова {word}: {len(word)}')

# students_scores = [3, 5, 4, 4, 2]

# avg_score = 0
# for score in students_scores:
#     avg_score = avg_score + score

# class_avg = avg_score / len(students_scores)    
# print(class_avg)

# stock = [
# 		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
#                 'discount': 25},
# 		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
#                 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]

# def discounted(price, discount, max_discaunt=30, phone_name=''):
#     price = abs(price)
#     discount = abs(discount)
#     max_discaunt = abs(max_discaunt)
#     if max_discaunt >= 100:
#         raise ValueError("Слишком большая максимальная скидка")
#     if discount >= max_discaunt:
#         return price
#     elif 'iphone' in phone_name.lower() or not phone_name:
#         return price
#     else:
#         return price-(price * discount / 100)

# for phone in stock:
#     phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])
# print(stock)

classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]
def count_class_avg(student_scores):
    score_summ = 0
    for score in student_scores:
        score_summ +=score
    return score_summ/len(student_scores)
school_avg_summ = 0
for one_class in classes:
    class_avg = count_class_avg(one_class['scores'])
    print(f'Средняя оценка класса {one_class["name"]}: {class_avg}')
    school_avg_summ +=class_avg

school_avg = round(school_avg_summ / len(classes), 1)
print(f'Средняя оцнка по школе: {school_avg}')
