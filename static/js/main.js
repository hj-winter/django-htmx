function userScroll() {
  const navbar = document.querySelector('.navbar');
  const toTopBtn = document.querySelector('#to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-sticky');
      toTopBtn.classList.add('show');
    } else {
      navbar.classList.remove('navbar-sticky');
      toTopBtn.classList.remove('show');
    }
  });
}

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

document.body.addEventListener("htmx:configRequest", (event) => {
  event.detail.headers["X-CSRFToken"] = "{{ csrf_token }}";
});

document.querySelector('#to-top').addEventListener('click', scrollToTop);
document.addEventListener('DOMContentLoaded', userScroll);
