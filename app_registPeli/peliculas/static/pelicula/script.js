// script.js

// Función para ver los detalles de una película
function verPelicula(N_id) {
    fetch(`/peliculas/ver/${N_id}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar la película');
            }
            return response.text();
        })
        .then(data => {
            // Aquí podrías mostrar los detalles en un modal o en otra parte de la página
            document.getElementById('detalleModal').innerHTML = data; // Por ejemplo
            $('#detalleModal').modal('show'); // Mostrar el modal (si estás usando Bootstrap)
        })
        .catch(error => console.error(error));
}

// Función para editar una película
function editarPelicula(N_id) {
    fetch(`/peliculas/editar/${N_id}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el formulario de edición');
            }
            return response.text();
        })
        .then(data => {
            // Aquí podrías mostrar el formulario de edición en un modal
            document.getElementById('editarModal').innerHTML = data; // Por ejemplo
            $('#editarModal').modal('show'); // Mostrar el modal
        })
        .catch(error => console.error(error));
}

// Función para eliminar una película
function eliminarPelicula(N_id) {
    if (confirm('¿Estás seguro de que deseas eliminar esta película?')) {
        fetch(`/peliculas/eliminar/${N_id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Necesitas la cookie CSRF para las solicitudes POST
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al eliminar la película');
                }
                return response.json(); // Suponiendo que envías un JSON de respuesta
            })
            .then(data => {
                // Aquí podrías actualizar la lista de películas en la página
                alert(data.message); // Mensaje de confirmación
                location.reload(); // Recargar la página para reflejar los cambios
            })
            .catch(error => console.error(error));
    }
}

// Función para obtener el valor de una cookie (necesario para CSRF)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Si esta cookie comienza con el nombre que buscamos, obtenemos su valor
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
