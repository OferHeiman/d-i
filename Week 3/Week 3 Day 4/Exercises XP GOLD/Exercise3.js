let verb = prompt("type a verb","") //1
    if(verb.length >= 3 && verb.slice(-3) != "ing") //2
    {
        console.log(verb + "ing")
    }
    else if(verb.length >= 3 && verb.slice(-3) == "ing") //3
    {
        console.log(verb + "ly")
    }
    else if(verb.length < 3) //4
    {
        console.log(verb)
  }