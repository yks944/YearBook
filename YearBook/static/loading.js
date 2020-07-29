
function load()
{   console.log($('#result').val());
    // $.post();
    $.ajaxStart();
    $.ajax({
        type: 'POST',
        url: 'year_book/add_s_achv/',
        data: {'data': 'data'},
        success:
            function (data) {
                if (data === 'Updated') {
                    document.getElementById('result').innerHTML = data;
                }
                else if (data === 'got exception') {
                    document.getElementById('result').innerHTML = "cannot add some internal problem occurred";
                }
            }
    });
}

$.ajaxSetup({
 beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}