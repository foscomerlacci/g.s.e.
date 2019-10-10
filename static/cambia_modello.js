/**
 * Created by utente on 28/08/18.
 */
$(document).ready(function() {
// ad ogni modifica del modello viene sbiancata la textbox "seriale"
            $(document).on('change', "select#id_modello", function(){

                     $("input#id_seriale").val("");
                 });

});