let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
function checkBasket() //1
{
let amazonItem=prompt("What item would you like to buy?"," ") //prompt the user for an item
if(amazonItem in amazonBasket) // let the user know if the item is in the basket
{
    alert("The item "+amazonItem+" is in the basket")
}
return;
}

checkBasket();