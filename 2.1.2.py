'''
Дана строка, возможно, содержащая пробелы. Напишите функцию определяющую является ли строка палиндромом,
считая что заглавные и строчные символы не различаются, а все не буквельные сиволы игнорируются.
Результат функции должен быть типа bool.
'''

def is_palindrome(string: str) -> bool:
    string_new = []
    for i in range(len(string)):
        if string[i].isalpha() == True:
            string_new.append(string[i].lower())
    for i in range(len(string_new)):
        if string_new[i] == string_new[-i - 1]:
            continue
        else:
            return(False)
    return(True)


