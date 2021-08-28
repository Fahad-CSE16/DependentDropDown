function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


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
        $("#id_division").change(function(){
            $.ajax({
                url:"/districts/",
                type:"POST",
                data:{division: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_district");
                    cols.options.length = 0;
                    cols.options.add(new Option("District", "District"));

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
        $("#id_district").change(function(){
            $.ajax({
                url:"/subdistricts/",
                type:"POST",
                data:{district: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_subdistrict");
                    cols.options.length = 0;
                    cols.options.add(new Option("Subdistrict", "Subdistrict"));
                    
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