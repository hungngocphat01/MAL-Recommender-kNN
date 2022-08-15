from __main__ import app
import models
from flask import render_template, request, url_for, redirect


@app.route('/', methods=['POST', 'GET'])
def home_page():
  # Handle user search submit action
  if request.method == 'POST':
    form = request.form
    query_string = form.get('query')
    return redirect(url_for('search_page', query=query_string))
  
  # Default behavior: render homepage template
  return render_template('home_page.html')


@app.route('/search')
def search_page():
  query_string = request.args.get('query')
  query_result = models.search_anime(query_string)
  result_iter = query_result.iterrows()

  return render_template('search_results.html', query=query_string, animes=result_iter)

@app.route('/recommend/<mal_id>')
def recommend_anime(mal_id):
  current_anime = models.get_anime(mal_id)
  recommend_ids = models.recommend_anime(current_anime.anime_id)
  recommend_animes = models.get_animes(recommend_ids)
  result_iter = recommend_animes.iterrows()

  return render_template('recommend.html', current_anime=current_anime, recommended=result_iter)
