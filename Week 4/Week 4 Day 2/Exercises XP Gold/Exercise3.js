function swapCase(userString) {
    let newString = '';
    for (let i = 0; i < userString.length; i++) {
        if (userString[i] === userString[i].toUpperCase()) {
            newString += userString[i].toLowerCase();
        }
        else {
            newString += userString[i].toUpperCase();
        }
    }
    console.log(newString);
}