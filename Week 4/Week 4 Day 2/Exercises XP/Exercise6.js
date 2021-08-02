let itemPrice=4.25;
let arrayChange=[25,20,5,0];
changeEnough(arrayChange,itemPrice);

function changeEnough(arrayChange,itemPrice)
{
let sumOfQuarters=arrayChange[0]*0.25;
let sumOfDimes=arrayChange[1]*0.10;
let sumOfNickels=arrayChange[2]*0.05;
let sumOfPennies=arrayChange[3]*0.01;
let sumOfAllCoins=(sumOfQuarters+sumOfDimes+sumOfNickels+sumOfPennies>=itemPrice) ? console.log(true) :  console.log(false);
}


