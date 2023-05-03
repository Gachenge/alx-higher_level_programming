const mylist = $('#add_item');
mylist.click(function () {
  const item = $('<li>').text('Item');
  $('ul.my_list').append(item);
});
