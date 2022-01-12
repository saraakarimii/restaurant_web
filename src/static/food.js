
    $("#popular").click(function() {
        console.log("clicked")
        send_ajax("popular_food")
        
    })
    $("#all").click(function() {
        console.log("clicked")
        send_ajax("all_food")
        
    })

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
    

   

    
    function send_ajax(input_data){
        console.log("ajaxsent")
        
        
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
                $('#ajax_f').empty()
                show_food(res)
   
            }
        });
    }

    function show_food(data,){
        
        my_main_tag = $('#ajax_f')
     
        
              
            
        if ( data['food'] ){
            for (const [key, value] of Object.entries(data['food'])) {
                console.log("*", key,value); 
                console.log(data['food'])
                

                
                 
                var div2= document.createElement("div"); 
                    div2.className="col-md-3";
                    var div3= document.createElement("div"); 
                    div3.className="product-block bg-light";
                    var Img = document.createElement("img");
                    Img.setAttribute('src', "https://fakeimg.pl/800x400/?retina=1&text=Product 1&font=noto");
                    Img.className="d-block w-100"
                    var food_name=document.createElement("h4");
                    food_name.append(value[0])
                    var branche=document.createElement("small");
                    branche.append(value[1])
                    var price=document.createElement("p");
                    price.append(value[2])
                    var sec_div=document.createElement("div");
                    sec_div.className="row"
                    var div4=document.createElement("div");
                    div4.className="col-md-6"
                    var div5=document.createElement("div");
                    div5.className="col-md-6"
                    var a1=document.createElement("a");
                    a1.className="btn btn-sm btn-success"
                    url_food='/costumer/branche/add_food/'+value[3]
                    a1.setAttribute('href',url_food)
                    a1.append('add to card')
                    var a2=document.createElement("a");
                    a2.className="btn btn-sm btn-danger"
                    url='costumer/branche/'+value[4]
                    a2.setAttribute('href',url)
                    a2.append("menu")
                    div5.append(a2)
                    div4.append(a1)
                    sec_div.append(div4)
                    sec_div.append(div5)
                    div3.append(Img,food_name,branche,price,sec_div)
                    div2.append(div3)
                    my_main_tag.append(div2)  
              
            }   
             }
        }
    