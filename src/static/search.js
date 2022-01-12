$( document ).ready(function() {

    // {{test}} error
    // console.log(test) error
    console.log(URL) 
    console.log(CSRF_TOKEN) 
    
    
        $("#in_text").on("input", function() {
            
            
            send_ajax($(this).val())
            
        });

        function send_ajax(input_data){
             
            data={
                'csrfmiddlewaretoken':CSRF_TOKEN,
                'text':input_data
                };
            // data['text'] = input_data
            console.log(data['text'])
    
            $.ajax({
                type: 'POST',
                // url: "http://127.0.0.1:8000/main/db_temp/",
                // url: "/main/db_temp/",
                url: URL,
                dataType: 'json',
                data:data,
                success: function(res) {
                    console.log(res);
                    show_foods(res)
                }
            })
        }

        function show_foods(data){
        
            my_sec_tag = $('#search_result')
            my_sec_tag.empty()
            if ( data['menu'] ){
                for (const [key, value] of Object.entries(data['menu'])) {
                    console.log("*", key, value);
                    // var main_div = document.createElement("div"); 
                    // main_div.className="container mt-5" ;
                    // var div1 = document.createElement("div"); 
                    // div1.className="row";

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
                    // div1.append(div2)
    
                    my_sec_tag.append(div2)
                    
                  }
                
            }else{
                my_sec_tag.empty()
               
            }
            
        }
    })
