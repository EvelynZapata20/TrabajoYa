// Evento para el botón de eliminar para mostrar un mensaje de confirmación
document.addEventListener("DOMContentLoaded", function () {
    const deleteButton = document.getElementById("botonEliminar");
    const deleteForm = document.getElementById("delete-form");

    deleteButton.addEventListener("click", function () {
        const confirmation = confirm("¿Seguro que quieres eliminar este registro?");
        if (confirmation) {
            deleteForm.submit();
        }
    });
});

// Evento para la carga de la imagen para mostrar la imagen seleccionada
$(document).ready(function() {
    const imageInput = $('[name="foto"]');
    const selectedImage = $('#selected-image');

    imageInput.on('change', function() {
        const input = this;
        if (input.files && input.files[0]) {
            const reader = new FileReader();

            reader.onload = function(e) {
                selectedImage.attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    });
})


// Evento para la calificación por estrellas
const starRating = document.querySelectorAll('.star-rating input');
starRating.forEach(input => {
    input.addEventListener('mouseenter', function () {
        input.parentNode.querySelectorAll('label').forEach((label, index) => {
            label.style.color = index < this.value ? '#FFD700' : '#ddd';
        });
    });

    input.addEventListener('mouseleave', function () {
        input.parentNode.querySelectorAll('label').forEach(label => {
            label.style.color = label.previousElementSibling && label.previousElementSibling.checked ? '#FFD700' : '#ddd';
        });
    });
});