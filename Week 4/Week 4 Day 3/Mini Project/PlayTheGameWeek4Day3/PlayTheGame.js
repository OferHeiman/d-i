function playTheGame() {
    if (!confirm("Would you like to play a game")) {
        alert("No problem, Goodbye.")
        return;
    }
    let computerNumber = Math.round(Math.random() * 10);
    let userNumber;
    let isNotValidNumber;
    for (let i = 0; i < 3; i++) {
        do {
            userNumber = parseInt(prompt("Please enter a number between 0 and 10"));
            isNotValidNumber = !userNumber || userNumber > 10 || userNumber < 0;
            isNotValidNumber = userNumber == 0 ? false : isNotValidNumber;
            if (isNotValidNumber) {
                alert("Sorry," + userNumber + " is not a valid number, please enter a number between 0 and 10");
            }
        }
        while (isNotValidNumber);
        if (test(userNumber, computerNumber)) {
            return;
        }
    }
    alert("out of chances");
    return;
}

function test(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
        alert("WINNER");
        return true;
    }
    if (userNumber > computerNumber) {
        alert("Your number is bigger than the computer's, guess again");
        return false;
    }
    if (userNumber < computerNumber) {
        alert("Your number is smaller than the computer's, guess again");
        return false;
    }
}