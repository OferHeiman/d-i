let stringOfNumbers = prompt("Please enter numbers separated by commas");
let arrayOfNumbers = stringOfNumbers.split(",");
let sumOfNumbers = 0;
for (i in arrayOfNumbers) {
    sumOfNumbers += parseInt(arrayOfNumbers[i]);
}
console.log(sumOfNumbers);