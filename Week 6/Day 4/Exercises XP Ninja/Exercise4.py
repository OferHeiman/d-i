def freq(str):
    str = str.split()         
    str2 = []
    for word in str:             
        if word not in str2:
            str2.append(word) 
    for word in str2:
        print('Frequency of', word, 'is :', str.count(word))    
        
string ='New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
freq(string)                    
  