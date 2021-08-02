function checkNumber() { //1
    for (let i = 0; i <= 100; i++) { //2
        if (i % 2 == 0) { //3
            console.log("The number " + i + " is even");
        }
        else {
            console.log("The number " + i + " is odd");
        }
    }
}
checkNumber() //4