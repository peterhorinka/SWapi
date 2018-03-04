

function buttonEvent() {
    let buttons = document.getElementsByClassName('residents');
    for(let button of buttons) {
        button.addEventListener('click', function () {
            getDataFromServer(button.id);
        });

    }
}

function getDataFromServer(planetName) {

    let url = 'https://swapi.co/api/planets';

    fetch(url)
    .then(response => response.json()) // parses response to JSON
    .then(function(resultedJsObject) {
        console.log('residents:', resultedJsObject);
    });


    // var xhr = new XMLHttpRequest();
    // xhr.open('GET', '/planetName');
    // xhr.onload = function () {
    //     if (xhr.status === 200) {
    //         alert('User\'s name is ' + xhr.responseText);
    //     }
    //     else {
    //         alert('Request failed.  Returned status of ' + xhr.status);
    //     }
    // };
    // xhr.send();
}

buttonEvent()