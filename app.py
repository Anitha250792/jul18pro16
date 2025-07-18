from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data by genre
movies_by_genre = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "Comedy": ["The Hangover", "Superbad", "Step Brothers"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"],
    "Horror": ["Get Out", "The Conjuring", "A Quiet Place"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

@app.route('/')
def index():
    genres = list(movies_by_genre.keys())
    return render_template('index.html', genres=genres)

@app.route('/pick', methods=['POST'])
def pick():
    selected_genre = request.form.get('genre')
    return redirect(url_for('show_movies', genre=selected_genre))

@app.route('/movies/<genre>')
def show_movies(genre):
    movie_list = movies_by_genre.get(genre, [])
    return render_template('movies.html', genre=genre, movies=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
