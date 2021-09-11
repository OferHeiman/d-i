def splitter(string, delimiter):
    result_list = []
    start = 0
    for index, char in enumerate(string):
        if char == delimiter:
            result_list.append(string[start:index])
            start = index + 1
    if start == 0:
        return [string]
    result_list.append(string[start:index + 1])
    return result_list

print(splitter('this1is1a1sentence','1'))