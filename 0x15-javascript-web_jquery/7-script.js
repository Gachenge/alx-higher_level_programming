fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
.then (response => response.json())
.then (data => {
    const name = data.name;
    $('#character').text(name);
});
