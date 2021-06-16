// objeto.metodo(json)

$("#formulario1").validate({
  rules: {
    txtnombre: {
      required: true,
      minlength: 3,
    },
    txtnombreusuario: {
      required: true,
      minlength: 4,
    },
    txtEmail: {
      required: true,
      email: true,
    },
    txtRepetirEmail: {
      required: true,
      equalTo: "#id_txtEmail",
    },
    txtContrasena: {
      required: true,
      minlength: 5,
    },
    txtRepetirContrasena: {
      required: true,
      equalTo: "#id_txtContrasena",
    },
  }, // --> Fin de reglas
  messages: {
    txtnombre: {
      required: "Ingrese nombre",
      minlength: "No cumple formato",
    },
    txtnombreusuario: {
      required: "Debe tener un nombre de usuario",
      minlength: "Debe tener minimo 4 carcteres",
    },
    txtEmail: {
      required: "Ingrese email",
      email: "No cumple formato",
    },
    txtRepetirEmail: {
      required: "Repita el email",
      equalTo: "Los emails no coinciden",
    },
    txtContrasena: {
      required: "Ingrese la contraseña",
      minlength: "Mínimo 5 caracteres",
    },
    txtRepetirContrasena: {
      required: "Repita la contraseña",
      equalTo: "Las contraseñas no coinciden",
    }, 
  },
  errorElement : 'div'
});