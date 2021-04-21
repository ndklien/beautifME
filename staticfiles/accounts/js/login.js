var input = document.getElementById("id_password");
var no_CAPSLOCK = document.getElementById("no_CAPSLOCK");
var text = document.getElementById("text");
input.addEventListener("keyup", function(event) {

if (!event.getModifierState("CapsLock")) {
    text.style.display = "none";
    no_CAPSLOCK.style.display = "block";
  } else {
    text.style.display = "block"
    no_CAPSLOCK.style.display = "none";
  }
});