# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    s=input()
    a,b=s.split(',')
    print(len(a)>len(b))
    print(a==b)
    print(a.find(b)!=-1)

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    s=input()
    print(s.strip())
    print(len(s))
    print(s.count('a', '@'))
    print(s.istitle())

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    s-input()
    print(s[1:-1])
    print(s[::2])
    print(s.lower()[::-1])

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    nums=list(map(int,input().split()))
    print(sorted(nums))
    print(sum(nums))
    print((min(nums), max (nums)))

# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    s=input()
    print(s.lower()==s.lower()[::-1]and ' 'not in s)

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    n = int(input())
    hex_str = hex(n)[2:]
    print(hex_str)
    print(len(hex_str))
    print('a' in hex_str)

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    n=int(input())
    print(months[n-1])
