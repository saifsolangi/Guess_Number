from flask import Flask, render_template, request
import random

computer_number = random.choice(range(1,5))

app = Flask(__name__)

guesses = []

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['number_guess'])
        message = check_number_show_message(guess, computer_number)
        guesses.append(message)
        return render_template('index.html', guesses= reversed(guesses))
        
    return render_template('index.html', guesses= reversed(guesses))

@app.route('/reset')
def reset():
    guesses.clear()
    return render_template('index.html')

def check_number_show_message(guessed_number, computer_number):
    if guessed_number < computer_number:
        return f"{guessed_number} is too low {random.choice(['⬇️', '👇'])}"
    elif guessed_number > computer_number:
        return f"{guessed_number} is too high {random.choice(['⬆️','👆🏻'])}"
    else:
        return f"{guessed_number} is correct {random.choice(['✅','🏆','🔥'])}"

app.run()