//Functions
// Exercise 1

// const MOM = 2;
// const DAD = 1.2;

// function DisplayParentsAge(MyAge) 
// {
//     let momage = MyAge*MOM
//     let dadage = momage*DAD
//     console.log("The Age of my mom is " + momage + ",The Age of my dad is "  + dadage)
// }
// DisplayParentsAge(25)

// Exercise 2

// const MOM_FACTORY = 2;
// function displayAgeOfMom(MyAge)
// {
// return MyAge*MOM_FACTORY;
// }
// console.log("The Age of my mom is: " + DisplayAgeOfMom(25))

//Arrow Functions
//Exercise 2 again
// const displayAgeOfMom = x => x*2
// console.log("The Age of my mom is: " + displayAgeOfMom(25))

//Object Methods

let person= {
    firstName : "Sarah",
    eyeColor: "blue",
    eat : function () {
        console.log("My name is " + this.firstName + " I love chocolate")
    }
}
person.eat()