//Exercise 2 part 1
let names = ["john","sarah",23,"Rudolf",34]
for (let i in names)
{
    if (typeof (names[i]) == "number") 
    {
        continue;
    }
    else if (typeof (names[i]) == "string") 
    {
        if (names[i][0] == names[i][0].toUpperCase()) 
        {
            continue;
        }
        else
        {
            console.log(names[i][0].toUpperCase() + names[i].slice(1))
        }
    }
}

//Exercise 2 part 2

// let names = ["john", "sarah", 23, "Rudolf", 34] 
// for (let i in names) {
//     if (typeof (names[i]) === "number") {
//         break;
//     }
//     else if (typeof (names[i]) === "string") {
//             console.log(names[i])
//         }
//     }



