function billDetails() {
    let bill = isNumberValid();
    let tip;
    if (bill < 50) {
        tip = bill * 0.2;
    }
    else if (bill >= 50 && bill <= 200) {
        tip = bill * 0.15;
    }
    else {
        tip = bill * 0.1;
    }
    let finalBill = bill + tip;
    console.log("Tip amount: " + tip+"\nFinal bill amount: " + finalBill);
}
billDetails();

function isNumberValid() //checks if number is 0 or bigger
{
    let num;
    let isNumberNotValid;
    do {
        num = prompt("What is the bill amount?", " ");
        isNumberNotValid = num.match(/^\d+$/gm) && num >= 0;
        if (!isNumberNotValid) {
            alert("Sorry," + num + " is not a valid bill amount,please enter a valid bill amount")
        }
    } while (!isNumberNotValid);
    return parseInt(num);
}