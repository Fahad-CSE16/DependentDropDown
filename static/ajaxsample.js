jQuery(function($){
    $(document).ready(function(){
        $("#id_country").change(function(){
            $.ajax({
                url:"/divisions/",
                type:"POST",
                data:{country: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_division");
                    cols.options.length = 0;
                    cols.options.add(new Option("Division", "Division"));
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": {{csrf_token}}
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
    }); 
});