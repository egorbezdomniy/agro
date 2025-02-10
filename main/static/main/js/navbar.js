document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.querySelector('.menu-toggle');
    const navbarRight = document.querySelector('.navbar-right');

    toggleButton.addEventListener('click', function () {
        navbarRight.classList.toggle('active');
    });
});
