def sum_over_k(sentence,k):
    sum = 0
    sentence = sentence.split(' ')
    for word in sentence:
        if len(word)>k:
            sum +=1
    print(sum)

sentence = 'Do or do not there is no try'
k=2
sum_over_k(sentence,k)