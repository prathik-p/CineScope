from django.shortcuts import render
from .utils import fetch_from_omdb 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# View to handle movie search requests
def search_movies_view(request):
    query = request.GET.get('q', '')  # Get search query from URL parameters
    movies_data = []
    error_message = None

    if query:
        # Search for movies by title using OMDb API
        api_response = fetch_from_omdb({'s': query, 'type': 'movie'})
        if api_response.get("Response") == "True":
            movies_data = api_response.get('Search', []) # Extract movie list
        else:
            error_message = api_response.get("Error", "Could not fetch results.")
    context = {
        'query': query,
        'movies': movies_data,
        'error_message': error_message,
    }
    return render(request, 'search_results.html', context)

# View to display details for a specific movie
def movie_detail_view(request, imdb_id):
    api_response = fetch_from_omdb({'i': imdb_id, 'plot': 'full'})  # Fetch full plot
    movie_details = None
    error_message = None

    if api_response.get("Response") == "True":
        movie_details = api_response
    else:
        error_message = api_response.get("Error", "Could not fetch movie details.")

    context = {
        'movie': movie_details,
        'error_message': error_message,
    }
    return render(request, 'movie_detail.html', context)

# View for the home page showing trending movies
def home_view(request):
    trending_movie_imdb_ids = [
        'tt0111161', # The Shawshank Redemption
        'tt0068646', # The Godfather
        'tt0468569', # The Dark Knight
        'tt0108052', # Schindler's List
        'tt1375666', # Inception
        'tt0816692', # Interstellar
    ]
    
    trending_movies_data = []
    poster_urls = [] 
    error_messages = []

    # Fetch details for each trending movie
    for imdb_id in trending_movie_imdb_ids:
        api_response = fetch_from_omdb({'i': imdb_id})
        if api_response.get("Response") == "True":
            trending_movies_data.append(api_response)
            # Collect poster URLs if available
            if api_response.get("Poster") and api_response["Poster"] != "N/A":
                poster_urls.append(api_response["Poster"])
        else:
            error_messages.append(f"Error fetching {imdb_id}: {api_response.get('Error')}")
    context = {
        'trending_movies': trending_movies_data,
        'errors': error_messages,
    }
    return render(request, 'home.html', context)

# View to handle favorite movies (supports POST for AJAX, GET for page)
@csrf_exempt
def favorites_view(request):
    if request.method == "POST":
        poster_urls = []
        error_messages = []
        movies = []
        # Parse list of IMDb IDs from request body
        imdb_ids = json.loads(request.body).get("imdb_ids", [])
        for imdb_id in imdb_ids:
            api_response = fetch_from_omdb({'i': imdb_id})
            if api_response.get("Response") == "True":
                movies.append(api_response)
                # Collect poster URLs if available
                if api_response.get("Poster") and api_response["Poster"] != "N/A":
                    poster_urls.append(api_response["Poster"])
            else:
                error_messages.append(f"Error fetching {imdb_id}: {api_response.get('Error')}")
        return JsonResponse({"movies": movies})
    else:
        # Render favorites page for GET requests
        return render(request, 'favorites.html')