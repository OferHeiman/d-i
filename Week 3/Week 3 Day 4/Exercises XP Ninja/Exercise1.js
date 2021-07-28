let age1 = parseInt(prompt("Which year were you born in?", ""))
let age2 = parseInt(prompt("Which year were you born im?", ""))
let dif = Math.abs(age1 - age2)
if (age1 > age2) 
{
    let year = age1 + dif
    console.log(" the date when the younger one is exactly half the age of the older is " + year)
}
else 
{
    let year = age2 + dif
    console.log(" the date when the younger one is exactly half the age of the older is " + year)
}