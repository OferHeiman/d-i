//part 1

function InfoAboutMe()
    {
console.log("My name is Ofer,i am 25 years old,my hobbies are watching movies and tv shows,playing video games,hanging out with my friends.")
    }
    InfoAboutMe()
    
    //part 2&3

    function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies)
    {
        console.log("Your name is " + personName + ",you are " + personAge + " years old," + "your favorite color is " + personFavoriteColor + ".")
        console.log("Your hobbies are:");
        for(let i in personHobbies)
        {
            console.log(personHobbies[i]);
        }
    }
    infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
    infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])



