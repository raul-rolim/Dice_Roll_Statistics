from die import Die
import pygal

while True:
    dies = []
    max_roll = 0
    quantity_die = int(input("Insert the quantity of dies you want to roll: "))
    for i in range(0, quantity_die, 1):
        
        while True:
            type_die = int(input("Types of dies available:\n-------------------\n| D4  | D6  | D8  |\n------------------- \n| D10 | D12 | D20 |\n-------------------\nType the respective number of the dice: "))
            condition1 = (type_die == 4) or (type_die == 6)
            condition2 = (type_die == 8) or (type_die == 10)
            condition3 = (type_die == 12) or (type_die == 20)

            if condition1 or condition2 or condition3:
                dies.append(Die(type_die))
                max_roll += type_die
                break
            else:
                print("Try Again")
    roll_input = int(input("How many times do you want to roll: "))

    results = []
    for roll in range(roll_input):
        roll_sum = 0
        for dice in dies:
            roll_sum += dice.roll()
        
        results.append(roll_sum)

    frequencies = []
    for frequency in range(len(dies), max_roll+1, 1):
        frequencies.append(results.count(frequency))

    labels = [str(value) for value in range(len(dies), max_roll+1, 1)]

    
    hist = pygal.Bar()
    hist.title = "Dice Rolling Statistics"
    hist.x_labels = labels
    hist._x_title = "Result"
    hist._y_title = "Frequency of Result"
    hist.add('D' + str(max_roll), frequencies)
    hist.render_to_file('die_visual.svg')