//one loop
for(i=1;i<=6;i++)
{
    console.log('*'.repeat(i));
}

//two loops
let star='';
for (i = 1; i <= 6; i++) 
{
    star = ''
    for (x = 1; x <= i; x++) 
    {
        star += '*'
    }
    console.log(star)
}