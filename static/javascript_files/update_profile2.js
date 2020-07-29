function update() {
    var username = document.getElementById("username");
    var email = document.getElementById("email");
    var enroll = document.getElementById("enroll");
    var address = document.getElementById("address");
    var mobile = document.getElementById("mobile");
    if(username==='' || email==='' || enroll==='' || address==='' || mobile==='')
    {
        document.getElementById("result").innerHTML='Please provide all input!!!';
    }
    else
    {
        var mydata = {'username':username,'address':address,'mobile':mobile};
        call(mydata);
    }
}
function call(mydata)
{
     $.ajax({
        type:'POST',
        url:'/year_book/update_profile/',
        data:mydata,
        success:
        function (data) {
        if (data==='Updated'){
            document.getElementById('result').innerHTML=data;
       }
        else if(data==='got exception')
       {
           document.getElementById('result').innerHTML="cannot add some internal problem occurred";
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
