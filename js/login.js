$(document).ready(function () {
    $("#contact-form").validate({
        rules: {
            name: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 6
            },
        },
        messages: {
            name: {
                required: "Ingrese usuario",
                minlength: "Largo minimo 6 caracteres"
            },
            password: {
                required: "Ingrese contraseña",
                minlength: "Largo minimo 6 caracteres"
            }
        },
        errorElement : 'div'
    });
});
