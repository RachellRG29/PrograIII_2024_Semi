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
