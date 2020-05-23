var modal = document.getElementById("myModal");

window.onload = function () {
    var views = Cookies.get('modal')
    if (views == null) {
        modal.style.display = "block"
    }
}

var moves = parseInt($('.moves').attr("value"));
var gold = parseInt($('.gold').attr("value"));
var winning_amount = parseInt($('.winning_amount').attr("value"));

if (moves < 0){
    var cheater = document.getElementById("cheater");
    window.onload = function(){
        cheater.style.display = "block"
    }
}

else if (moves == 0 && winning_amount < 0 && gold <= winning_amount){
    var pauper = document.getElementById("pauper");
    window.onload = function(){
        pauper.style.display = "block"
    }
}

else if (moves == 0 && gold < 0) {
    var bankrupt = document.getElementById("bankrupt");
    window.onload = function () {
        bankrupt.style.display = "block"
    }

} else if (moves == 0 && gold <= winning_amount) {
    var loser = document.getElementById("loser");
    window.onload = function () {
        loser.style.display = "block"
    }

} else if (moves == 0 && gold >= winning_amount && winning_amount > 0) {
    var winner = document.getElementById("winner");
    window.onload = function () {
        winner.style.display = "block"
    }
}
 else if (moves == 0 && gold >= winning_amount && winning_amount < 0) {
    var lazy = document.getElementById("lazy");
    window.onload = function () {
        lazy.style.display = "block"
    }
}

$(".new_game").click(function () {
    Cookies.set("modal", "viewed");
})

$("a.try_again").click(function () {
    Cookies.remove("modal");
})

var textarea = document.getElementById('activity');
textarea.scrollTop = textarea.scrollHeight;