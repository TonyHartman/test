'''
Напишите функцию возвращающую число вхождений подстроки в строку.
Я считал, что они не пересекаются. Те для строки asasasasa ответ 2
'''
def sub_strings(s: str, sub: str) -> int:
    print(str.count(sub))
str = input()
sub = input()
sub_strings(str, sub)