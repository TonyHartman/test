def polindrom(string):
    for i in range(len(string)):
        string_new = string.lower()
        if string_new[i] == string_new[-i - 1]:
            continue
        else:
            return(False)
    return(True)