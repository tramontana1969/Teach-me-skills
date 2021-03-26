import os
from dotenv import load_dotenv


load_dotenv()

items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')
print(items, sum, order_num)

# 1. Поменяем номер очереди с суммой местами, присвоив переменным значения из окружения
sum = os.getenv('ORDER_NUM')
order_num = os.getenv('SUM')
print(items, sum, order_num)

# 2. Посчитаем среднюю стоимсть каждой пиццы в заказе
items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')

average_price =float(sum)/int(items)
print('средняя стоимсть каждой пиццы в заказе:', average_price, 'дбл')

# 3. В сумме заказа имеется дробь. Если бы требовалось преобразовать целое число в дробное, воспользовался бы командой "float"
# Пример:
sum = float(sum)
print(sum)

# 4. Покольку у клиента в номере заказа есть цифра 2, ему положена скидка в 50%:
discount = int(sum)*50/100
print('Поздравляем! \nВы нарвались на аттракцион невиданной щедрости, и вам положена скидка 50%. \nСтоимость Вашего заказа составит', discount, 'дбл')

# 5. Если бы колличество пицц в заказе составляло бы меньше 2, номер в очереди следовало бы сократить на 5. Сделать это можно следующим образом:
new_order_num = round(int(order_num)/5)
print (new_order_num)