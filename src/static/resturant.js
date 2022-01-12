
    
    $("#restaurant").click(function() {
        
        send_ajaxx("resturan")
        
    })


    
    function send_ajaxx(input_data){
        
        
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
               console.log("r*********essss")
               $('#ajax_r').empty()
                show_res(res)
   
            }
        });
    }

    function show_res(data){
           
            
        if ( data['resturan'] ){
            for (const [key, value] of Object.entries(data['resturan'])) {
                console.log("*", key,value); 
                console.log(data['resturan'])
                
                    my_main_tag = $('#ajax_r')
               

                
                 
                    var div1= document.createElement("div"); 
                    div1.className="col-md-3 ";
                    var div2= document.createElement("div"); 
                    div2.className="product-block bg-light";
                    var branche=document.createElement("h4");
                    branche.append(value[0]);

                    var a1=document.createElement("a");
                    a1.className="btn btn-sm btn-danger";
                    pk=value[1];
                    url='costumer/branche/'+pk
                    console.log(url)
                    a1.setAttribute('href',url);
                    a1.append("menu");
                    // var sec_div=document.createElement("div");
                    // sec_div.className="row"
                    // var div3=document.createElement("div");
                    // div3.className="col-md-6  bg-light";
                    // div3.append(a1)
                    // sec_div.append(div3)
                    div2.append(branche,a1);
                    div1.append(div2);
                    my_main_tag.append(div1);


              
            }   
             }
        }
    