//1
document.querySelector('div').style = 'background-color:lightblue ; padding: 5px;';
//2
document.querySelector('ul').children[0].style = 'display: none';
//3
document.querySelector('ul').children[1].style = 'border: solid';
//4
document.body.style.fontSize = "32px"
//5
if(document.querySelector('div').style.backgroundColor == 'lightblue')
{
    alert("Hello "+document.querySelector('ul').children[0].innerText+" and "+document.querySelector('ul').children[1].innerText)
}