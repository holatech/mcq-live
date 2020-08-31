let counter = 180;
    setInterval(function(){
        counter--;
        if(counter >= 0){
            id = document.getElementById('counts');
            id.innerHTML = counter;
        }

        if(counter == 0){
            document.getElementById('submit').click()
        }
    }, 1000);