#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)

    return sum_list

stopper = "k"
finished = False
s = 0
while not finished:
    num_str_user = input("Введите числа, разделяя пробелом: ")
    s += sum_nums(num_str_user, stopper)
    finished = stopper in num_str_user
    print(f"сумма = {s}")
