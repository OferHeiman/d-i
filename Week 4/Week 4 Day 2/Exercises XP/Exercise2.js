let age = prompt("How old are you?"," ") //1
function checkDriverAge(age) //2
{
    if(age<18)
    {
        alert("Sorry, you are too young to drive this car. Powering off")
    }
    else if(age>18)
    {
    alert("You are old enough to drive, Powering On. Enjoy the ride!")
    }
    else
    {
        alert("Congratulations on your first year of driving. Enjoy the ride!")
    }
}

checkDriverAge(age) //3
checkDriverAge(25) //4
