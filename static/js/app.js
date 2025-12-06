// DELETE NOTE FUNCTION (RESTful DELETE)
async function deleteNote(noteId) {
    const confirmDelete = confirm("Are you sure you want to delete this note?");
    if (!confirmDelete) return;

    const response = await fetch(`/notes/${noteId}`, {
        method: "DELETE"
    });

    if (response.ok) {
        alert("Note deleted successfully.");
        location.reload();
    } else {
        alert("Error deleting note.");
    }
}

// Auto-submit search bar when typing
function autoSearch() {
    const form = document.getElementById("searchForm");
    form.submit();
}
