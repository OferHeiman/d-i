// let sentence = ["The","dinner","is","not","that","bad","!","you","cook","well"]
let sentence = ["The","dinner","is","not","so","bad"]
// let sentence = ["The","dinner","is","bad"] 
let wordnot = sentence.indexOf("not") 
let wordbad = sentence.indexOf("bad")
if(wordbad > wordnot && wordnot != -1) 
{
    sentence.splice(wordnot,(wordbad - wordnot)+1,"good")
    console.log(sentence)
}
else if(wordbad < wordnot || wordnot == -1)
{
    console.log(sentence)
}
