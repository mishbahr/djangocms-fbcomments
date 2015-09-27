(function($) {
    $(function() {
        $(':input[name="load_trigger"]').change(function() {
            var buttonTextField = $('.form-row.field-button_text');
            $(this).val() == 'click' ? buttonTextField.slideDown() : buttonTextField.slideUp();
        }).change();
    });
})(django.jQuery);
