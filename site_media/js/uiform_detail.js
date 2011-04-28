// Prevents CSRF for AJAX
$('html').ajaxSend(function(event, xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });

$(function() {
        $(".delete-link").click(function(e) {
                e.preventDefault();
                if (confirm("Are you sure you want to delete this field? There is no undo.")) {
                    console.log("confirmed");
                    var field = $(e.currentTarget).parents("div.uiformfield")[0];
                    var field_id = parseInt(field.id);
                    console.log(field_id);
                    var url = window.location.pathname;
                    $.post(
                           url,
                           {'id': field_id},
                           function(data, textStatus, jqXHR) {
                               if (data == "success"){
                                   $(field).slideToggle('fast');
                               } else {
                                   console.log("it failed.");
                               }
                           });
                }
            });

        $('#email-submit').click(function(e) {
                e.preventDefault();
                alert("No email will actually be sent. The email_link function in views.py works, but requires and SMTP server and some settings filled out in settings.py");
            });
    });