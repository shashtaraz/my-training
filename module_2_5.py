# def get_matrix():
#     result_1 = get_matrix(2, 2, 10)
#     result_2 = get_matrix(3, 5, 42)
#     result_3 = get_matrix(4, 2, 13)
# print(result_1)
#
# matrix = []

# простая функция
def say_hello():
    print('Hello')
# вызов функции:
say_hello()
say_hello()
say_hello()

# ПРИНИМАЮЩАЯ функция
def say_hello(name):    # - name - параметр
    print('Hello', name)
# вызов функции:
say_hello('Sasha')
say_hello('Jahan')
say_hello('Anna')
say_hello('Anna')
say_hello('Anna')

# ВОЗВРАЩАЮЩАЯ функция
import random
def lottery():
    tickets = [1,2,3,4,5,6,7,8,9]
    win = random.choice(tickets)
    return win   # - проекращение работы функции
win = lottery()
win_1 = lottery() + lottery()
print(win)
print(win_1)

# И ПРИНИМАЮЩАЯ И ВОЗВРАЩАЮЩАЯ функция
import random
def lottery(mon, thue):
    tickets = [1,2,3,4,5,6,7,8,9]
    win_3 = random.choice(tickets)
    tickets.remove(win_3)
    win_4 = random.choice(tickets)
    print(mon, thue)
    return win_3, win_4   # - проекращение работы функции

win_3, win_4 = lottery(mon: 'mon', thue: 'thue')
print(win_3, win_4)

