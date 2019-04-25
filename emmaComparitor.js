const shitIGotInStock = ['some', 'food', 'things'];
const meals = [{'mealName1':['some','things','other'],'mealName2':['food','some','things']}]

meals.map((meal) => {
    if (shitIGotInStock.indexOf(meal)) {
    console.log(meal);
  }
});