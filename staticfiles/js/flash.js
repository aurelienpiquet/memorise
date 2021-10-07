
function removeFlashes() {
    myVar = setTimeout(function() {     
        flash_messages = document.querySelector('.messages');
        if (flash_messages) {
            flash_messages.style.transform = 'translateY(-200px)';
            flash_messages.style.opacity = '0';
    }}, 1000);
}     

removeFlashes()


