"""Марина Кожарская
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
ss = int(input('введите количество секунд: '))

if ss < 60:
    print(f"00:00:{ss}")
elif ss < 3600:
    print(f"00:{ss // 60}:{ss % 60}")
else:
    print(f"{ss // 3600:02}:{(ss % 3600) // 60:02}:{ss % 60:02}")
