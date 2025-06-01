// Key used to store favorite movie IDs in localStorage
const FAVORITES_KEY = "movieExplorerFavorites";

/* Retrieves the array of favorite movie IDs from localStorage.*/
function getFavoriteMovieIds() {
    const favorites = localStorage.getItem(FAVORITES_KEY);
    return favorites ? JSON.parse(favorites) : [];
}

/* Saves the array of favorite movie IDs to localStorage.*/
function saveFavoriteMovieIds(movieIds) {
    localStorage.setItem(FAVORITES_KEY, JSON.stringify(movieIds));
}

/* Checks if a movie is in the favorites list.*/
function isMovieFavorite(imdbID) {
    const favorites = getFavoriteMovieIds();
    return favorites.includes(imdbID);
}

/* Adds a movie to the favorites list if not already present.*/
function addMovieToFavorites(imdbID) {
    const favorites = getFavoriteMovieIds();
    if (!favorites.includes(imdbID) && imdbID != null && imdbID != undefined) {
        favorites.push(imdbID);
        saveFavoriteMovieIds(favorites);
        console.log(`Added ${imdbID} to favorites.`);
        return true; // Indicate success
    }
    console.log(`${imdbID} is already a favorite.`);
    return false; // Indicate already present
}

/* Removes a movie from the favorites list if present. */
function removeMovieFromFavorites(imdbID) {
    let favorites = getFavoriteMovieIds();
    if (favorites.includes(imdbID)) {
        favorites = favorites.filter((id) => id !== imdbID);
        saveFavoriteMovieIds(favorites);
        console.log(`Removed ${imdbID} from favorites.`);
        return true; // Indicate success
    }
    console.log(`${imdbID} was not in favorites.`);
    return false; // Indicate not found
}

/* Toggles the favorite status of a movie and updates the button state.*/
function toggleFavorite(imdbID, buttonElement) {
    if (isMovieFavorite(imdbID)) {
        removeMovieFromFavorites(imdbID);
        if (buttonElement) {
            buttonElement.classList.toggle("active");
        }
    } else {
        addMovieToFavorites(imdbID);
        if (buttonElement) {
            buttonElement.classList.toggle("active");
        }
    }
}

/* Updates the button state to reflect whether the movie is a favorite. */
function updateFavoriteButtonState(imdbID, buttonElement) {
    if (buttonElement) {
        if (isMovieFavorite(imdbID)) {
            buttonElement.classList.toggle("active");
        }
    }
}
