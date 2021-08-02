let stock = {  //1
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppinglist=["banana","orange","apple"]; //2

function myBill() //3
{
let totalprice=0;
    if(stock.banana>0)
    {
totalprice=totalprice+prices.banana;
stock.banana--; //6
    }
    if(stock.orange>0)
    {
totalprice=totalprice+prices.orange;
stock.orange--; //6
    }
    if(stock.apple>0)
    {
totalprice=totalprice+prices.apple;
stock.apple--; //6
    }
    console.log("The total price of your bill is: "+totalprice); //4
return totalprice;
}

myBill();//5
