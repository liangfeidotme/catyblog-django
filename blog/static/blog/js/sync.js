/**
 * Created by lyndon on 6/4/14.
 */
$(function() {
    /* get categories */
    var json_gate_way = $('#json-gateway').attr('value');
    /* get recent posts*/
    var url = json_gate_way.replace('get_type', 'recent');
    var $recent_list = $('#recent-list');
    var article_link = $recent_list.attr('value');

    $recent_list.empty();
    $.getJSON(url, function(data) {
        $.each(data, function(i, item) {
            var html = '<li><a href="'
                    + article_link.replace('0', item.id)
                    + '">'
                    + item.title
                    + '</a></li>';
            $recent_list.append(html);
        });
    });

    $('button#search').click(function() {
        var keyword = $('input#keyword').val();
        var url = $(this).attr('value');
        url = url.replace('keyword', keyword);
        window.open(url, '_self');
    });


    // using jQuery
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
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var update_comments = function() {
        var url = $('#json-gateway').attr('value').replace('get_type', 'comment');
        var $comment_list = $("#comment-list");
        var $new_item = $comment_list.find("#comment-template").clone();
        $comment_list.children().remove();
        $.getJSON(url, function(data) {
            $.each(data, function(i, item) {
                $new_item = $new_item.clone();
                $new_item.find("h4").text(item.mail);
                $new_item.find("p").text(item.comment);
                $comment_list.append($new_item);
            });
        });
    }
    update_comments();
    // Attach a submit handler to the form
    $("#comment-form").submit(function(event) {
        // Stop form from submitting normally
        event.preventDefault();

        // Get some values from elements on the page:
        var $form = $(this),
        url = $form.attr( "action" );

        // Send the data using post
        var posting = $.post(url, $form.serialize());

        // Put the results in a div
        posting.done(function( data ) {
            $form.find('textarea').val('');
            update_comments();
        });
    });
});