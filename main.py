HST = 0.13
labour_cost = 0.75
rent_cost = 1.00
materials_cost_per_inch = 0.50
def calculate_subtotal(diameter):
    subtotal = labour_cost + rent_cost + (materials_cost_per_inch * diameter)
    tax = subtotal * HST
    total = subtotal + tax
    return (subtotal, 2), (total, 2)
diameter = game.ask("Enter the diameter of the pizza: ", "")
subtotal, total = calculate_subtotal (diameter)
game.splash("Subtotal: $" + subtotal)
game.splash("Total: $" + total)