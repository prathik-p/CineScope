document.addEventListener("DOMContentLoaded", function () {
  const favButtons = document.getElementsByClassName(
    "material-symbols-outlined"
  );
  console.log("Favorite buttons found:", favButtons);
  Array.from(favButtons).forEach(function (favButton) {
    const imdbID = favButton.dataset.imdbid;
    console.log("IMDB ID for favorite button:", imdbID);

    // Initialize button state on page load
    updateFavoriteButtonState(imdbID, favButton);

    favButton.addEventListener("click", function () {
      toggleFavorite(imdbID, this);
    });
  });
});
