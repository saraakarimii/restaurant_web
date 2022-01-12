$( document ).ready(function() {
    $("#popular").click(function() {
        console.log("ffff")
        send_ajax("food")
        
    })
    $("#popularr").click(function() {
        
        send_ajax("resturan")
        
    })

})
    
    function send_ajax(input_data){
        console.log(input_data)
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
             "value":input_data,
        };
       
        $.ajax({
            type: 'POST',
          
            url: URL,
            dataType: 'json',
            data:data,
            success: function(res) {
               console.log("fine")
                $('#ajax_f').empty()
                $('#ajax_r').empty()
                $('#foodl').empty()
                $('#resl').empty()
                show_tasks(res,input_data)
   
            }
        });
    }

    function show_tasks(data,i){
        if (i=='food'){
            my_ul_tag = $('#ajax_f')
        }
        else{
            my_ul_tag = $('#ajax_r')
        }
        console.log(my_ul_tag)
        if (my_ul_tag.children().length==0){
            
                var th1 = document.createElement("th");
                th1.append("name")
                // var th2 = document.createElement("th");
                // th2.append("category")  
                // var th3 = document.createElement("th");
                // th3.append("title")
                // var th4 = document.createElement("th");
                // th4.append("timing#")
                // var th5 = document.createElement("th");
                // th5.append("description")
                
                my_ul_tag.append(th1)
              
        }
              
            
        if ( data['food'] ){
            for (const [key, value] of Object.entries(data['food'])) {
                console.log("*", key,value); 
                console.log(data['food'])
                if (i=='food'){
                    my_ul_tag = $('#foodl')
                }
                else{
                    my_ul_tag = $('#resl')
                }

                
                 
                var th1 = document.createElement("th");
                th1.append(value[0])
                // var th2 = document.createElement("th");
                // th2.append(value[1])  
                // var th3 = document.createElement("th");
                // th3.append(value[2])
                // var th4 = document.createElement("th");
                // th4.append(value[3])
                // var th5 = document.createElement("th");
                
                // th5.append(value[4])
                var tr=document.createElement("tr");
                tr.append(th1)
                my_ul_tag.append(tr)  
              
            }   
             }
        }
    