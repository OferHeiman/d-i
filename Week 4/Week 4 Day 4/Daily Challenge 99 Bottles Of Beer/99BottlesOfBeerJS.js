let numBeers=IsNumOfBeersValid();
BottlesOfBeer(numBeers);
console.log("Thank you for playing 99 Bottles Of Beer");

function BottlesOfBeer(numBeers) {
    if(numBeers==1)
    {
        console.log(numBeers + " bottle of beer on the wall")
        console.log(numBeers + " bottle of beer");
        console.log("Take the last one down,pass it around");
        console.log("No more bottles of beer on the wall, no more bottles of beer.");
    }
   else
   {
    for (let i = 1; i < numBeers; i++)
     {
        if(i==1)
        {
            console.log(numBeers + " bottles of beer on the wall")
            console.log(numBeers + " bottles of beer");
            console.log("Take " + i + " down,pass it around");
            numBeers = numBeers - i;
            if(numBeers>1)
            {
            console.log(numBeers + " bottles of beer on the wall");
            }
            else
            {
                console.log(numBeers + " bottle of beer on the wall");
            }
        }
        else
        {
            console.log(numBeers + " bottles of beer on the wall")
            console.log(numBeers + " bottles of beer");
            console.log("Take " + i + " down,pass them around");
            numBeers = numBeers - i;
            if(numBeers>1)
            {
            console.log(numBeers + " bottles of beer on the wall");
            }
            else
            {
                console.log(numBeers + " bottle of beer on the wall");
            } 
        }
    }
    if(numBeers>=2)
        {
            console.log(numBeers + " bottles of beer on the wall");
            console.log(numBeers + " bottles of beer");
            console.log("Take the last " + numBeers + " down,pass them around, no more bottles of beer on the wall.");
            console.log("No more bottles of beer on the wall, no more bottles of beer.");
        }
        else
        {
            console.log(numBeers + " bottle of beer on the wall");
            console.log(numBeers + " bottle of beer");
            console.log("Take the last one down,pass it around");
            console.log("No more bottles of beer on the wall, no more bottles of beer.");
        }
}
    if (confirm("Do you want to keep playing 99 Bottles of beer?", "")) 
    {
        console.log("Go to the store and buy some more");
        numBeers = prompt("How many more bottles of beer do you want to buy?", "")
        while (numBeers<1)
        {
            numBeers = prompt("Please buy at least 1 bottle of beer,How many more bottles of beer do you want to buy?", "")
        }
        return BottlesOfBeer(numBeers);
    }
    else {
        return;
    }
}

function IsNumOfBeersValid()
{
    let numBeers;
    let isNumOfBeersNotValid;
    do {
        numBeers = prompt("How many bottles of beer do you want to buy?","")
        isNumOfBeersNotValid = numBeers.match(/^\d+$/g) && numBeers>0;
        if (!isNumOfBeersNotValid)
        {
            alert("Sorry," + numBeers + " is not a valid number of bottles,please buy at least 1 bottle of beer")
        }
    } while (!isNumOfBeersNotValid);
return numBeers;
}
