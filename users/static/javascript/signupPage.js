function checkUser(username) {
    return $.ajax({
        type: 'GET',
        url: "http://localhost:8000/users/check_username_exists",
        data: { username: username }
    });
}

$(document).ready(function() {
    $('#myForm').submit(function(event) {
        event.preventDefault();

        const username = $('#username').val();
        const usernameErrorSpan = $('#username-error');
        const usernameInput = $('#username');
        usernameInput.on('input blur', function() {
            usernameErrorSpan.text('');
        })

        checkUser(username).done(function(response) {
            if (response === "true") {
                // Username exists
                usernameErrorSpan.text('Username already exists');
                usernameErrorSpan.show();
            } else if (response === "false") {
                // Username is available, hide error message
                usernameErrorSpan.hide();
                // Submit the form
                $('#myForm').off('submit').submit();
            } else if (response === "error") {
                // Handle error case
                usernameErrorSpan.text('');
                alert('Something went wrong. Please try again.');
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error('AJAX Error:', textStatus, errorThrown);
            // Handle AJAX request failure
            usernameErrorSpan.text('');
            alert('Something went wrong. Please try again.');
        });
    });
});
