let zip = prompt("What is your zip code?","")
zip.match(/^[0-9]{4}\S$/) ? console.log("Success") : console.log("Error")
// if(zip.match(/^[0-9]{4}\S$/))
// {
//     console.log("Success")
// }
// else
// {
//     console.log("Error")
// }