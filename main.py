import os
from dotenv import load_dotenv

load_dotenv()

items = int(os.getenv('ITEMS'))
sum = float(os.getenv('SUM'))
order_num = int(os.getenv('ORDER_NUM'))
print(items, sum, order_num)

# 1. Поменяем № очереди с суммой местами.
# sum, order_num = order_num, sum
# print('1', items,sum,order_num)

# 2. Посчитаем среднюю стоимсть каждой пиццы в заказе.
print('2. Средняя стоимсть каждой пиццы в заказе:', sum / items)

# 3. В сумма заказа - десятичное число, преобразуем его в целое
print('3.', int(sum // 1))

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%:
if order_num % 10 == 2 or order_num % 100 // 10 == 2 \
        or order_num % 1000 // 100 == 2:
    print(
        '4. Поздравляем! \nВы нарвались на аттракцион невиданной щедрости,'
        'и вам положена скидка 50%. \nСтоимость Вашего заказа составит',
        sum * 50 / 100)
else:
    print('4. Скидка не положена')

# 5. Если количество пицц в заказе составляет меньше 2, номер в очереди
# сократим на 5. Сделать это можно следующим образом:
if items < 2:
    print(order_num - 5)
else:
    print("5. Очередь не сокарщается")
