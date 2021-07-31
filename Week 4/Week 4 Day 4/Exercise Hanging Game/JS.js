function Hangman() ////////////////////////////////////////////////////////////////////////////////////////////////////////
{
    let Player2Letter;
    Player1Word = isWordValid();
    let ListOfPlayer2Letters = "";
    let Regex;
    let HangmanWord = Player1Word.replaceAll(/./g, "*");
    for (let i = 0; i < 10; i++) 
    {
        Player2Letter = isPlayer2LetterValid(ListOfPlayer2Letters);
        ListOfPlayer2Letters = ListOfPlayer2Letters + Player2Letter;
        console.log("You tried the letters:" + ListOfPlayer2Letters)
        if (Player1Word.includes(Player2Letter)) {
            Regex = new RegExp("(?![" + ListOfPlayer2Letters + "])[a-z]", "g");
            HangmanWord = Player1Word.replaceAll(Regex, '*');
            i--;
        }
        console.log(HangmanWord)
        if (!HangmanWord.includes("*")) {
            alert("You Win")
            console.log("You Win");
            return;
        }
    }
    console.log("YOU LOSE")
    return;
}
Hangman()

function isWordValid() //////////////////////////////////////////////////////////////////////////////////////////////////////
{
    let Player1Word;
    let isWordNotValid;
    do {
        Player1Word = prompt("Type a word with minimum 8 letters", " ").toLowerCase();
        isWordNotValid = Player1Word.match(/^[a-z]{8,}$/);
        if (!isWordNotValid) {
            alert("Sorry," + Player1Word + " is not a valid word,please enter a word with minimum 8 letters")
        }
    } while (!isWordNotValid)
    console.log(Player1Word.replaceAll(/./g, "*"))
    return Player1Word;
}

function isPlayer2LetterValid(ListOfPlayer2Letters) ///////////////////////////////////////////////////////////////////////////
{
    let Player2Letter;
    let isLetterNotValid;
    do {
        Player2Letter = prompt("Type a letter which hasn't been guessed before", " ").toLowerCase();
        isLetterNotValid = Player2Letter.match(/^[a-z]{1}$/g) && !ListOfPlayer2Letters.includes(Player2Letter);
        if (!isLetterNotValid) {
            alert("Sorry," + Player2Letter + " is not a valid letter,please enter a letter which hasn't been guessed before")
        }
    } while (!isLetterNotValid)
    return Player2Letter;

}

