/**
 * Created by utente on 07/06/18.
 */
(function($) {

    //al caricamento della pagina nascondo il div con all'interno la class assegnata a to_hide

    $(document).ready(function() {
        var
            to_hide = $('.form-row.field-tecnico_consegna.field-inizio_prestito');

        to_hide.hide(1);

    });
})(django.jQuery);


