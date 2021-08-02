function hotel() //1
{
    let numNights = isNumberOfHotelNightsValid();
    let totalPriceOfHotel = numNights * 140;
    return totalPriceOfHotel;
}
function planeRideCost() //2
{
    let destination = isDestinationValid();
    let priceOfPlaneRide;
    if (destination.match('London')) {
        priceOfPlaneRide = 183;
    }
    else if (destination.match('Paris')) {
        priceOfPlaneRide = 220;
    }
    else {
        priceOfPlaneRide = 300;
    }
    return priceOfPlaneRide;
}
function rentalCarCost()//3
{
    let numDaysRentingCar = isNumberOfCarRentDaysValid();
    let priceOfRentingCar = numDaysRentingCar > 10 ? (numDaysRentingCar * 40) * 0.95 : numDaysRentingCar * 40;
    return priceOfRentingCar;
}
function totalVacationCost()//4
{
    let priceOfPlaneRide = planeRideCost();
    let totalPriceOfHotel = hotel();
    let priceOfRentingCar = rentalCarCost();
    let totalCost = priceOfRentingCar + totalPriceOfHotel + priceOfPlaneRide;
    console.log("The car cost: $" + priceOfRentingCar + "\nthe hotel cost: $" + totalPriceOfHotel + "\nthe plane ticket cost: $" + priceOfPlaneRide + "\nfor a total cost of: $" + totalCost);
}
function isNumberOfCarRentDaysValid() //checks if number is 0 or more
{
    let num;
    let isNumberNotValid;
    do {
        num = prompt("For how many days would you like to rent the car?", "");
        isNumberNotValid = num.match(/^\d+$/gm) && num >= 0;
        if (!isNumberNotValid) {
            alert("Sorry," + num + " is not a valid number of days to rent the car,please enter a valid number of days to rent the car")
        }
    } while (!isNumberNotValid);
    return num;
}
function isNumberOfHotelNightsValid() //checks if number is 0 or more
{
    let num;
    let isNumberNotValid;
    do {
        num = prompt("How many nights would you like to stay in the hotel?", "");
        isNumberNotValid = num.match(/^\d+$/gm) && num >= 0;
        if (!isNumberNotValid) {
            alert("Sorry," + num + " is not a valid number of nights,please enter a valid number of nights")
        }
    } while (!isNumberNotValid);
    return num;
}
function isDestinationValid() //check if destination valid
{
    let Destination;
    let isDestinationNotValid;
    do {
        Destination = prompt("What is your destination?", " ");
        isDestinationNotValid = Destination.match(/[a-zA-Z]+$/gm);
        if (!isDestinationNotValid) {
            alert("Sorry," + Destination + " is not a valid destination,please enter a valid destination")
        }
    } while (!isDestinationNotValid)
    return Destination;
}

totalVacationCost(); //5