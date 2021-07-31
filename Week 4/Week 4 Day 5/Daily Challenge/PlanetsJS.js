let PlanetsArray = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'] //1
for(let i in PlanetsArray)
{
    let newDiv=document.createElement("div"); //2
    newDiv.className = "planet"; //2
    newDiv.innerText = PlanetsArray[i];
    newDiv.style.backgroundColor=random_bg_color(); //3
    document.body.firstElementChild.appendChild(newDiv); //4
}



function random_bg_color() 
{
    let x = Math.floor(Math.random() * 256);
    let y = Math.floor(Math.random() * 256);
    let z = Math.floor(Math.random() * 256);
    let bgColor = "rgb(" + x + "," + y + "," + z + ")";
    return bgColor;
    }