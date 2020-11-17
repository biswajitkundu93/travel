 $(() => {
        setInterval(() => {
          $(".card").fadeOut("slow").fadeIn(2000);
        }, 8000);
      });
      function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
      }

      function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
      }
      function openNav2() {
        document.getElementById("mySidenav2").style.width = "250px";
      }

      function closeNav2() {
        document.getElementById("mySidenav2").style.width = "0";
      }
      
window.onscroll = function() {myFunction()};
var navbar = document.getElementById("nav_scroll");
function myFunction() {
  if (window.pageYOffset >= 200) {
    navbar.classList.add("sticky-navbar")
  } else {
    navbar.classList.remove("sticky-navbar");
  }
}