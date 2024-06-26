const treeContainer = document.getElementById("tree");

document.addEventListener("DOMContentLoaded", function () {
  getcategory(); 
});

function createInput(type, labelContent, name, value) {
    const input = document.createElement('input');
    const label = document.createElement('label');
  
    input.setAttribute('type', type);
    input.setAttribute('name', name);
  
    if (type === 'radio') {
      input.setAttribute('value', value);
    }
  
    label.innerHTML = labelContent;
  
    return [label, input];
  }
  
  function makeForm(fields, form) {
    for (const field of fields) {
      const fieldType = field[1];
      const fieldValues = field[0];
  
      for (const value of fieldValues) {
        const [label, input] = createInput(
          fieldType === 0 ? 'number' : fieldType === 1 ? 'text' : fieldType === 2 ? 'file' : 'radio',
          value,
          value, 
          fieldType === 3 ? value : '' 
        );
        form.appendChild(label);
        form.appendChild(input);
      }
    }
  }

function getcategory() {

    const url = 'http://127.0.0.1:8000/seller/product-manager/create/category';
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        
        createTree(data, treeContainer);
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
}

function createTree(array, parent) {
    
    for (const data of array) {
        const sublist = document.createElement("li");

        if (Array.isArray(data)) {
            const radioInput = document.createElement("input");
            radioInput.type = "radio";
            radioInput.name = "myRadioGroup";
            radioInput.value = data[1]; // Set the value of the radio button
            

            const radioLabel = document.createTextNode(data[0]);

            const radioLabelElement = document.createElement("label");
            radioLabelElement.appendChild(radioInput);
            radioLabelElement.appendChild(radioLabel);

            // Add a click event listener to the radio button
            radioInput.addEventListener("click", function () {
                sendCategory(data[1]); // Call a function to send the value to the server
            });

            sublist.appendChild(radioLabelElement);
            parent.appendChild(sublist);
        }
        else {
            const key = Object.keys(data)[0];
            sublist.textContent = key;
            const subitem = document.createElement("ul");
            createTree(data[key], subitem);
            sublist.appendChild(subitem);
            parent.appendChild(sublist);
        }
    }
}

function sendCategory(category) {
    const url = 'http://127.0.0.1:8000/seller/product-manager/create/category';
    const dataToSend = { category: category };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', // Set the content type to JSON
            'X-CSRFToken': csrfToken, // Include the CSRF token from the JavaScript variable
        },
        body: JSON.stringify(dataToSend), // Convert data to JSON
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
    
            const formContainer = document.getElementById('form-container');
            const previousForm = formContainer.querySelector('form');
            if (previousForm) {
                previousForm.remove();
            }
            const form = document.createElement('form');

            form.enctype = 'multipart/form-data';
            makeForm(data, form);
        
            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken'; 
            csrfTokenInput.value = csrfToken;
            
            const submitButton = document.createElement('input');
            submitButton.type = 'button';
            submitButton.value = 'Submit';

            submitButton.addEventListener("click", function () {
                sendProductForm(form); // Call a function to send the value to the server
            })

            formContainer.appendChild(form);
            form.appendChild(csrfTokenInput);
            form.appendChild(submitButton);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

}

function sendProductForm(form) {
    
    const formData = new FormData(form);
    const url = 'http://127.0.0.1:8000/seller/product-manager/create';

    fetch(url, {
        method: 'POST',
        headers: {
            
            'X-CSRFToken': csrfToken, // Include the CSRF token from the JavaScript variable
        },
        body: formData, 
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
        
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}