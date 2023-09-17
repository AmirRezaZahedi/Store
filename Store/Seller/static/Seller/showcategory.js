<<<<<<< HEAD
=======

//import { sendSelectedValueToServer } from './Getradio.js'
import { sendSelectedValueToServer } from "./Getradio.js";
>>>>>>> 289b7b09ebc5dcd08b7921f05c275629ecc43e51
const treeContainer = document.getElementById("tree");

document.addEventListener("DOMContentLoaded", function () {
  getcategory(); 
});

function getcategory() {
<<<<<<< HEAD
    const url = 'http://127.0.0.1:8000/seller/product-manager/create/category';
=======
    const url = 'http://127.0.0.1:8000/seller/product-manager/create/sendcategory';
>>>>>>> 289b7b09ebc5dcd08b7921f05c275629ecc43e51
    console.log(url);
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

export function sendSelectedValueToServer(selectedValue) {
    const url = 'http://127.0.0.1:8000/seller/product-manager/create/category';
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

        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

}
