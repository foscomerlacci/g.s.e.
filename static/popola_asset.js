/**
 * Created by utente on 23/04/18.
 */



// inspect html to check id of category select dropdown.
            $(document).on('focusin', "select#id_asset", function(){
                $.getJSON("/get_Asset/",{id: $("select#id_fk_beneficiario").val()}, function(j){
                     var options = '<option value="">---------</option>';

                     for (var i = 0; i < j.length; i++) {
                         options += '<option value="' + j[i][0] + '">' + j[i][1] + " (" + j[i][2] + ") " +'</option>';
                     }
                     // alert(options);
// inspect html to check id of subcategory select dropdown.
                     $("select#id_asset").html(options);

                 });
             });

