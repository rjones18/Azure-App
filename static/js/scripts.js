document.querySelectorAll('.btn-primary').forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        alert('You clicked Read More!');
    });
});


  