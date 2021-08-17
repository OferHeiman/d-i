import re
matrix=[
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!'],
    ]
def decrypt_matrix(matrix):
    matrix_string = ''
    for i in range(len(matrix[0])):
        decoded_matrix_column=[''.join(str(x[i]) for x in matrix)]
        matrix_string += ''.join(decoded_matrix_column)
    matrix_string = re.sub("[^a-zA-Z]{2,}"," ",matrix_string)
    matrix_string = re.sub("[^a-zA-Z\s]","",matrix_string)
    print(matrix_string)  
decrypt_matrix(matrix)