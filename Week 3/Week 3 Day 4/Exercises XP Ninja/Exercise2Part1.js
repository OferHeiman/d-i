let zip = prompt("What is your zip code?","")
if(zip.length == 5 && typeof parseInt(zip,10) == "number" && zip.indexOf(" ") == -1)
{
    console.log("Success")
}
else
{
    console.log("Error")
}