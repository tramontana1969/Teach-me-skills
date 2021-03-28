import os
from dotenv import load_dotenv

load_dotenv()

items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')
print(items, sum, order_num)

# 1. Поменяем № очереди с суммой местами.
# sum, order_num = order_num, sum
# print('1', items,sum,order_num)

# 2. Посчитаем среднюю стоимсть каждой пиццы в заказе.
print('2. Средняя стоимсть каждой пиццы в заказе:', float(sum) / int(items))

# 3. В сумма заказа - десятичное число, преобразуем его в целое
print('3.', int(float(sum) // 1))

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%:
if int(order_num) % 10 == 2 or int(order_num) % 100 // 10 == 2 \
        or int(order_num) % 1000 // 100 == 2:
    print(
        '4. Поздравляем! \nВы нарвались на аттракцион невиданной щедрости,'
        'и вам положена скидка 50%. \nСтоимость Вашего заказа составит',
        float(sum) * 50 / 100)
else:
    print('4. Скидка не положена')

# 5. Если количество пицц в заказе составляет меньше 2, номер в очереди
# сократим на 5. Сделать это можно следующим образом:
if int(items) < 2:
    print(int(order_num) - 5)
else:
    print("5. Очередь не сокарщается")
