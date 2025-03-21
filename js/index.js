// Toggle menu items visibility
const menuIcon = document.getElementById('menuIcon');
const menuItems = document.getElementById('menuItems');

if (menuIcon && menuItems) {
  menuIcon.addEventListener('click', () => {
    menuItems.classList.toggle('show'); // Ensure 'show' is lowercase in CSS
  });
}

// Automatically update the copyright year
document.addEventListener("DOMContentLoaded", function () {
  const yearElement = document.getElementById("year");
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }
});
