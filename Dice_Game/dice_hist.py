from dice import Dice
import pygal
dice = Dice()
results=[]
for roll_num in range(1000):

# stores the results for each single dice roll in a list
    result = dice.roll()
    results.append(result)

# analyze the results
frequencies = []

# range starts at 0, increments by 1 and stops just before the last number
# Uses +1 to stop just before 7 for 1-6 sides

for value in range(1, dice.dice_sides +1):
    
# call the value as you count the results
    frequency = results.count(value)
# similar to the results list, keep appending or adding the frequency
    frequencies.append(frequency)

# Print the frequencies to the Python Shell
print(frequencies)

# creates a bar chart to display the results
char = pygal.Bar()

# use your name in the bar chart's title

char.title = "(Antonio's Results from 1000 Dice Rolls"
# This section describes the labels for the bars in a bar chart
# You can change these labels, but for your first run, see how the chart looks first.

char.x_labels = ["1", "2", "3", "4", "5", "6"]
char.x_title = "Result" # displays at the bottom of the chart
char.y_title = "How Often Did We Roll a 1, 2, 3, 4, 5, or 6?"

char.add("D6", frequencies)
char.render_to_file("dice_barchart.svg")


