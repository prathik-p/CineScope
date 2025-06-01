window.addEventListener('scroll', function () {
        var menuToggle = document.getElementById('menuToggle');
        var navContainer = document.querySelector('.nav-container');
        if (window.scrollY > 100) {
        menuToggle.style.display = 'block';
        navContainer.style.display = 'none';
        } else {
        menuToggle.style.display = 'none';
        navContainer.style.display = 'flex';
        }
      });
      // Set initial state
      document.addEventListener('DOMContentLoaded', function () {
        var menuToggle = document.getElementById('menuToggle');
        var navContainer = document.querySelector('.nav-container');
        menuToggle.style.display = 'none';
        navContainer.style.display = 'flex';
      });