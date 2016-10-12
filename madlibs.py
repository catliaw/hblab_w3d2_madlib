from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)
    # compliment = ", ".join(compliments)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Show playgame response"""

    game_on = request.args.get('playgame')

    if game_on == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib', methods=["GET"])
def show_madlib():
    """Show madlib game result"""

    # madlib_stories = ["There once was a <b>{{ color }} {{ noun }}</b> sitting in the Hackbright Lab. When <u>{{ person }}</u> went to pick it up, it burst into flames in a totally <i>{{ adjective }}</i> way.", "{{ person }}, the {{ color }} {{ noun }} was a very popular {{ noun }} -- the most {{ adjective }} {{ noun }}."]

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjectives = request.args.getlist('adjectives')

    madlib_choices = ["madlib1.html", "madlib2.html"]
    madlib_text = choice(madlib_choices)

    # madlib_text = choice(madlib_stories)

    return render_template(madlib_text, 
                            person = person, 
                            color = color,
                            noun = noun, 
                            adjectives = adjectives)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
