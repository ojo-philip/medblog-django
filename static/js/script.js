// navbar
const navBtn = document.querySelector('.nav-btn')
const linkContainer = document.querySelector('.links-container')
const navBarItem = document.querySelector('.navbar-item')


navBtn.addEventListener('click', function () {
  let linkContainerHeight = linkContainer.getBoundingClientRect().height;
  let navBarItemHeight = navBarItem.getBoundingClientRect().height;
  if (linkContainerHeight == 0) {
    linkContainer.style.height = `${navBarItemHeight}px`;
  } else {
    linkContainer.style.height = 0
  }
})
// scroll top
const scrollTop = document.querySelector('.scroll-top')
const navBar = document.querySelector('#navbar')
window.addEventListener('scroll', function () {
  let navBarHeight = navBar.getBoundingClientRect().height;
  let scrollHeight = window.pageYOffset;
  if (scrollHeight > navBarHeight) {
    navBar.classList.add('fixed-nav')
  } else {
    navBar.classList.remove('fixed-nav')

  }
  if (scrollHeight > 500) {
    scrollTop.classList.add('show-item');
  } else {
    scrollTop.classList.remove('show-item');

  }

})
// footer year
let blogYear = document.querySelector('.year');
let year = new Date().getFullYear();
blogYear.textContent = year