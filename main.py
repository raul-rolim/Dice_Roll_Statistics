from die import Die
import pygal

class Main:

    def __init__(self):
        pass

    def create_dies(self):
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
        return dies, max_roll
    
    def roll_input(self):
        roll_input = int(input("How many times do you want to roll: "))
        return roll_input
    
    def roll_dies(self, roll_input, dies):
        results = []
        for roll in range(roll_input):
            roll_sum = 0
            for dice in dies:
                roll_sum += dice.roll()
            
            results.append(roll_sum)
        return results

    def obtain_frequencies(self, dies, max_roll, results):
        frequencies = []
        for frequency in range(len(dies), max_roll+1, 1):
            frequencies.append(results.count(frequency))

        labels = [str(value) for value in range(len(dies), max_roll+1, 1)]
        return labels, frequencies, 

    def create_histogram(self, labels, frequencies, max_roll):
        hist = pygal.Bar()
        hist.title = "Dice Rolling Statistics"
        hist.x_labels = labels
        hist._x_title = "Result"
        hist._y_title = "Frequency of Result"
        hist.add('D' + str(max_roll), frequencies)
        hist.render_to_file('die_visual.svg')

main = Main()
while True:
    dies, max_roll = main.create_dies()
    user_roll_input = main.roll_input()
    results = main.roll_dies(user_roll_input, dies)
    labels, frequencies = main.obtain_frequencies(dies, max_roll, results)
    main.create_histogram(labels, frequencies, max_roll)
    close_program = input("Again? (y/n): ")
    if close_program == 'n':
        break
