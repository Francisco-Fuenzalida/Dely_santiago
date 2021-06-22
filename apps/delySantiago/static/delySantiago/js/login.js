$(document).ready(function () {
    $("#contact-form").validate({
        rules: {
            name: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 4
            },
        },
        messages: {
            name: {
                required: "Ingrese usuario",
                minlength: "Largo minimo 3 caracteres"
            },
            password: {
                required: "Ingrese contraseña",
                minlength: "Largo minimo 4 caracteres"
            }
        },
        errorElement : 'div'
    });
});