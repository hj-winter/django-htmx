setTimeout(function() {
  $("#message").fadeOut("slow");
}, 3000);

const clearBtn = document.querySelector("#clear");

clearBtn.addEventListener("click", () => alert("Clear items"));

document.body.addEventListener("htmx:configRequest", (event) => {
  event.detail.headers["X-CSRFToken"] = "{{ csrf_token }}";
});
document.addEventListener("DOMContentLoaded", function() {
  setTimeout();
});
