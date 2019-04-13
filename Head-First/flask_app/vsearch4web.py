from flask import Flask, render_template, request
from functions import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters.search_for_letters(phrase, letters))
    return render_template('results.html',
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
