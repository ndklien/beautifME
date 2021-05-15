function myFunction() {
    var x = document.getElementById("cbp-hrmenu");
    if (x.className === "cbp-hrmenu") {
      x.className += " responsive";
    } else {
      x.className = "cbp-hrmenu";
    }
  }