fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies = data.results.map(movie => movie.title);
    const ul = $('<ul>');
    movies.forEach(title => {
      const li = $('<li>').text(title);
      ul.append(li);
    });
    $('#list_movies').append(ul);
  });
