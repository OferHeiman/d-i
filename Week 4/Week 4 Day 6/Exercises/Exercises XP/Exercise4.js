let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
  let userName = prompt("What is your name? ");
  if(userName in guestList){
      console.log("Hi! I'm "+userName+", and I'm from "+guestList[userName]);
  }
  else{
      console.log("Hi! I'm a guest.");
  }