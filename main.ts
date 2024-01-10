game.splash("Lets calulate the cost of a pizza")
let Diameter = game.askForNumber("What is the diameter of the pizza?")
let HST = 1.13
let labour_cost = 0.75
let rent_cost = 1
let materials_cost_per_inch = 0.5
let subtotal = materials_cost_per_inch * Diameter + labour_cost + rent_cost
let tax = subtotal * HST
let Total_Cost = tax
game.splash("the subtotal is", subtotal)
game.splash("The total cost is", tax)
