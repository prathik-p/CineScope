# CineScope - Movie Explorer Django App

CineScope is a web application built with Django that allows users to search for movies, view detailed information, see a list of pre-defined "trending" movies, and manage a personal list of favorite movies using browser localStorage. Movie data is fetched from the OMDb API.

## Features

- **Movie Search:** Search for movies, series, and episodes by title.
- **Date Filtering:** Filter search results by type (Movie, Series, Episode, or Any).
- **Movie Details:** View comprehensive details for a selected movie, including poster, plot, ratings, director, actors, etc.
- **Trending Movies:** A homepage section showcasing a curated list of popular movies with a background poster slideshow.
- **Favorites System:** Add movies to a personal favorites list or remove them. Favorites are stored locally in the user's browser (no login required).
- **Responsive Design:** Basic responsive styling for usability across different screen sizes.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **API:** OMDb API (The Open Movie Database)
- **Data Storage (Favorites):** Browser LocalStorage
- **HTTP Requests:** `requests` Python library (backend), `fetch` API (frontend)
- **Environment Variables:** `python-dotenv`

## Prerequisites

- Python 3.8+
- Pip (Python package installer)
- A web browser

## Setup and Installation

Follow these steps to set up and run the CineScope application locally:

**1. Clone the Repository (or Download the Source Code)**

If you have the project in a Git repository:

```bash
git clone <repository-url>
cd movie-explorer-project-directory
```

Otherwise, ensure you have all the project files in a local directory.

**2. Create and Activate a Virtual Environment**

It's highly recommended to use a virtual environment to manage project dependencies.

- For macOS/Linux:

```python
python3 -m venv venv
source venv/bin/activate
```

- For Windows:

```python
python -m venv venv
.\venv\Scripts\activate
```

You should see (venv) at the beginning of your terminal prompt, indicating the virtual environment is active.

**3. Install Dependencies**

Install all required Python packages using the requirements.txt file:

```
pip install -r requirements.txt
```

This will install Django, requests, python-dotenv, and any other necessary libraries.

**4. Get an OMDb API Key**

This application requires an API key from OMDb to fetch movie data. The free tier is sufficient for this project.

- Go to the OMDb API Key page: http://www.omdbapi.com/apikey.aspx
- Select the "FREE!" plan.
- Enter your email address and follow the instructions. You will receive an API key via email.

**5. Configure Environment Variables**

Create a .env file in the root directory of the project (the same level as `manage.py`). Add your OMDb API key to this file:

```
OMDB_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

Replace YOUR_ACTUAL_API_KEY_HERE with the API key you received from OMDb.

**6. Apply Database Migrations**

Although this project primarily uses OMDb for data and localStorage for favorites (not requiring extensive database use for core features), Django projects typically have initial migrations for built-in apps (like admin, auth, sessions).

```
python manage.py makemigrations
python manage.py migrate
```

**7. Run the Development Server**

Start the Django development server:

```
python manage.py runserver
```

By default, the server will run on http://127.0.0.1:8000/.
