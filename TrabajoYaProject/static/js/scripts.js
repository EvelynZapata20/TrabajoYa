// Event for the delete button to show a confirmation message
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