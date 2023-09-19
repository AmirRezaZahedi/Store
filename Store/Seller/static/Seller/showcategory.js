const treeContainer = document.getElementById("tree");

document.addEventListener("DOMContentLoaded", function () {
  getcategory(); 
});
function make_form(formData, type, form) {
  for (const field of formData) {

    const input = document.createElement('input');
    input.setAttribute('type', type);
    input.setAttribute('name', field);
    input.setAttribute("required", "required");
    //input.setAttribute('value', formData[key]);
    form.appendChild(input);
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
                sendSelectedValueToServer(data[1]); // Call a function to send the value to the server
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

function sendSelectedValueToServer(selectedValue) {
    const url = 'http://127.0.0.1:8000/seller/product-manager/create';
    const dataToSend = { selectedCategory: selectedValue };

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
            const int = data[0]
            const char = data[1]
            const img = data[2]

            const formContainer = document.getElementById('form-container');
            const previousForm = formContainer.querySelector('form');
            if (previousForm) {
                previousForm.remove();
            }
            const form = document.createElement('form');
            form.action = '';
            form.method = 'POST';
            make_form(int, 'number', form);
            make_form(char, 'text', form);
            make_form(img, 'file', form);

            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken'; 
            csrfTokenInput.value = csrfToken;
            
            const submitButton = document.createElement('input');
            submitButton.type = 'submit';
            submitButton.value = 'Submit';

            submitButton.addEventListener("click", function () {
                send_productForm(form,int,char,img); // Call a function to send the value to the server
            });

            formContainer.appendChild(form);
            form.appendChild(csrfTokenInput);
            form.appendChild(submitButton);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

}

function send_productForm(form, intFields, charFields, imgFields) {

    int = { field: form for field of intFields }
    char = { field: form for field of charFields }
    img = { field: form for field of imgFields }
    dataToSend=[int,char,img]
    const url = 'http://127.0.0.1:8000/seller/product-manager/create';

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
        
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

}