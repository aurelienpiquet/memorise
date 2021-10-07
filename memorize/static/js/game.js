
function removeGame() {
    myVar = setTimeout(function() {     
        game = document.querySelector('.game');
        if (game) {
            game.style.transform = 'translateX(-1300px)';
            game.style.opacity = 1;
    }}, 500);
}     

removeGame()



