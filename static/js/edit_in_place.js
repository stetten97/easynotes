const edit_button = document.querySelectorAll(".edit-button");
const note = document.querySelectorAll(".note")

edit_button.forEach((button, index) => {
    button.addEventListener("click", () => {
        const newContent = prompt("Edit the note:", note[index].textContent);

        if (newContent != null) {
            fetch(`/edit_note/${note[index].dataset.noteid}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({note_content: newContent}),

            })
            .then(response => response.json())
            .then(data => {
                if (data.message == "Note Update Successfull!") {
                    note[index].textContent = newContent;
                } else {
                    alert("Failed to update note!")
                }
            })
            .catch(error => {
                console.error('Error', error);
                alert('Failed to update note!')
            });
        }
    });
});