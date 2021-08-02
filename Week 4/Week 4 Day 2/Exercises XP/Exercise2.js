let age = isAgeNumberValid(); //1
function checkDriverAge(age) //2
{
    if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off")
    }
    else if (age > 18) {
        alert("You are old enough to drive, Powering On. Enjoy the ride!")
    }
    else {
        alert("Congratulations on your first year of driving. Enjoy the ride!")
    }
}

function isAgeNumberValid() // checks if age is a number
{
    let age;
    let isAgeNumberNotValid;
    do {
        age = prompt("How old are you?", " ");
        isAgeNumberNotValid = age.match(/^\d+$/gm);
        if (!isAgeNumberNotValid) {
            alert("Sorry," + age + " is not a valid age,please enter a valid age")
        }
    } while (!isAgeNumberNotValid);
    return age;
}

checkDriverAge(age); //3
checkDriverAge(25); //4
