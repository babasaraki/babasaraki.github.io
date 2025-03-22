const menuIcon = document.getElementById('menuIcon');
const menuItems = document.getElementById('menuItems');

menuIcon.addEventListener('click', () => {
  menuItems.classList.toggle('show');
});
