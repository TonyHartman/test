def months_list(list1):
    ans = [(list1[i] % 17) for i in range(len(list1))]
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    for i in range(len(ans)):
        if ans[i] <= 12:
            ans[i] = months[i]
    print(ans)

