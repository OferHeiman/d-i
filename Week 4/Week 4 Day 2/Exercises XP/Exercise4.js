function isDivisible(divisor) 
{ 
    let sum=0;
    for (let i = 0; i <=500; i++) 
    {
        if (i%divisor == 0) 
        { 
            sum=sum+i;
            console.log(i); 
        }
    }
    console.log(sum) 
}
isDivisible(100) 