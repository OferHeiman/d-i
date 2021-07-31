//1
let element=document.getElementById("navBar")
element.setAttribute("id","socialNetworkNavigation")
//2
let newli=document.createElement("li");
newli.appendChild(document.createTextNode("Logout"));
element.firstElementChild.appendChild(newli);
//3
console.log(element.firstElementChild.firstElementChild.textContent);
console.log(element.firstElementChild.lastElementChild.textContent);