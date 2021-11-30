/*
const executeUnit = document.querySelectorAll(".execute-unit");
const revisExecuteUnits = document.querySelectorAll(".revise-execute-unit");
const revisExecuteInput = document.querySelectorAll(".revise-execute-unit");

for (let i = 1; i < revisExecuteInput.length; i++) {
  revisExecuteInput[i].addEventListener("input", () => {});
}

function revise_data(cellIndex, learningDetailID) {
  executeUnit[cellIndex].classList.add("hidden");
  revisExecuteUnits[cellIndex].classList.remove("hidden");
}

function revise_data_onchange(event) {}
*/

///// navbar
let arrow = document.querySelectorAll(".arrow");

for (let i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e) => {
    let arrowParent = e.target.parentElement.parentElement;

    arrowParent.classList.toggle("showMenu");
  });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");

sidebarBtn.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});

// Schedule Slider
$(".schedule-content").owlCarousel({
  margin: 25,
  mouseDrag: false,
  nav: true,
  animateIn: "flipInX",
  animateOut: "fadeOut",
  navText: ["<i class='fas fa-chevron-left'></i>", "<i class='fas fa-chevron-right'></i>"],
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
  },
});

setTimeout(function () {
  $("#message").fadeOut("slow");
}, 3000);
