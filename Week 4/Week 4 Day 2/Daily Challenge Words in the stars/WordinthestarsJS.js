let words = prompt("Write several words separated by commas").split(",");
words = words.map(word => word.trim());//trim spaces and turn into array
let longestWord = "";
for (i = 0; i < words.length; i++) //checks which word is the longest
{
    if (words[i].length > longestWord.length) {
        longestWord = words[i];
    }
}
console.log("*".repeat(longestWord.length + 4)); //line of stars
for (i = 0; i < words.length; i++)//star at the start,word,whitespaces,star at the end
{
    console.log("* " + words[i] + (" ".repeat(longestWord.length - words[i].length)) + " *");
}
console.log("*".repeat(longestWord.length + 4)); //line of stars