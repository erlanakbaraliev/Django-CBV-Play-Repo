function load_content(event) {
    // event.preventDefault()
    const url = $(this).attr("data-url")
    $.ajax({
        url: url,
        type: 'get',
        success: function(responseHtml){
            $("#main").html(responseHtml)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(errorThrown)
        },
    })
}

$( document ).ready(function() {
    $(".nav-action").on("click", load_content)
});