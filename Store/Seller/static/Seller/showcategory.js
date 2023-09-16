//import { sendSelectedValueToServer } from './getradio.js';
import { sendSelectedValueToServer } from './getradio.js'
const treeContainer = document.getElementById("tree");

document.addEventListener("DOMContentLoaded", function () {
  getcategory(); 
});

function getcategory() {
    const url = 'http://127.0.0.1:8000/seller/product-manager/create/getcategory';

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

    if (typeof data === "string") {
      const radioInput = document.createElement("input");
      radioInput.type = "radio";
      radioInput.name = "myRadioGroup";
      radioInput.value = data; // Set the value of the radio button

      const radioLabel = document.createTextNode(data);

      const radioLabelElement = document.createElement("label");
      radioLabelElement.appendChild(radioInput);
      radioLabelElement.appendChild(radioLabel);

      // Add a click event listener to the radio button
      radioInput.addEventListener("click", function () {
        sendSelectedValueToServer(data); // Call a function to send the value to the server
      });

      sublist.appendChild(radioLabelElement);
      parent.appendChild(sublist);
    } else {
      const key = Object.keys(data)[0];
      sublist.textContent = key;
      const subitem = document.createElement("ul");
      createTree(data[key], subitem);
      sublist.appendChild(subitem);
      parent.appendChild(sublist);
    }
  }
}

