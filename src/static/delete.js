$("#delete").click(function() {
    console.log("clicked")
    send_ajax("deletee")
    
})

function send_ajax(input_data){
        
        
    data={
        'csrfmiddlewaretoken':CSRF_TOKEN,
         "value_r":input_data,
    };
   
    $.ajax({
        type: 'POST',
      
        url: URL,
        dataType: 'json',
        data:data,
        success: function(res) {
           
            show_res(res)

        }
    });
}