function editInPlace(button, editable, identifier, property_name, url_template) {
    button.forEach((button, index) => {
        button.addEventListener("click", () => {
            const newContent = prompt("Edit the note:", editable[index].textContent);

            if (newContent != null) {
                const data = {};
                data[property_name] = newContent

                fetch(`${url_template}${editable[index].dataset[identifier]}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message)
                    if (data.message ==  `${identifier} Update Successfull!`) {
                        editable[index].textContent = newContent;
                    } else {
                        alert(`Failed to update ${identifier}!`)
                    }
                })
                .catch(error => {
                    console.error('Error', error);
                    alert(`Failed to update ${identifier}!`)
                });
            }
        });
    });
}

const edit_button = document.querySelectorAll(".edit-button");
const note = document.querySelectorAll(".note")
const notebook = document.querySelectorAll(".notebook")
const url_template_notebook = "/rename/"
const url_template_note = "/edit/"

editInPlace(edit_button, note, "noteid", "note_content", url_template_note)
editInPlace(edit_button, notebook, "notebookid", "notebook_name", url_template_notebook)