$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    
    create_post();
});


function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#youtubeUrl').val() }, // data sent with the post request
        dataType: 'json',
        // handle a successful response
        success : function(json) {
             $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
             console.log("success"); // another sanity check
             $('#result').html(JSON.stringify(json));
             var base_url = window.location.origin;
    //           $('#result').html("<video width='320' height='240' controls>"+
				//   "<source src=' {{ STATIC_URL }}' ' type='video/mp4'>"+
				// "</video>");

    			$('#result').html('<video width="320" height="240" controls>'+
				  '<source  src="'+base_url+'/static/media/temp.mp4" type="video/mp4">'+
				'</video>');
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
