//--- LOGICA DEL SCRIPT DEL LOGIN----
//boton cerrar advertencia login error contra o usuario
function closeDialog() {
    document.getElementById('warning-dialog-login').style.display = 'none'; 
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const errorMessage = urlParams.get('error');

    if (errorMessage) {
        document.getElementById('error-message').innerText = errorMessage;
        document.getElementById('warning-dialog-login').style.display = 'block';
    }
};

function handleSubmit() {
    return true; // Permite el envío del formulario
}

//visile la contra
/*function togglePassword() {
    const passwordInput = document.getElementById('password');
    const passwordIcon = document.getElementById('password-icon');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        passwordIcon.classList.remove('fa-eye');
        passwordIcon.classList.add('fa-eye-slash'); // Cambia al icono de ojo cerrado
    } else {
        passwordInput.type = 'password';
        passwordIcon.classList.remove('fa-eye-slash');
        passwordIcon.classList.add('fa-eye'); // Cambia al icono de ojo abierto
    }
}*/