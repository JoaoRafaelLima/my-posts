

function deletar(id){
    window.location.href = "/deletar/"+id;
}
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
console.log(csrftoken);

function curtir(id_post){
    //window.location.href = "/curtir/"+id;
    
 
    let request = $.ajax({

        url:  `/curtir/`,
        type:  'POST',
        headers:{ "X-CSRFToken": csrftoken },
        data: {
            'id_post': id_post
        },
        dataType:  'json',
        
    });
    request.done(function teste(){
        window.location.href = "/";
    
    })
    //window.location.href = "/";

}