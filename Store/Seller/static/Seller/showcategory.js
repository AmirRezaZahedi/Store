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
        addRadioButtonClass();
        runSecondScript();
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

      const radioLabel = document.createTextNode(data);

      const radioLabelElement = document.createElement("label");
      radioLabelElement.appendChild(radioInput);
      radioLabelElement.appendChild(radioLabel);

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

function addRadioButtonClass() {
  const radioButtons = document.querySelectorAll("input[type='radio']");
  radioButtons.forEach(radio => {
    radio.classList.add("radio-button");
  });
}
function runSecondScript() {
  const radioButtons = document.querySelectorAll(".radio-button");
  radioButtons.forEach(radio => {
    radio.addEventListener("click", function() {
      if (radio.checked) {
        const sendData = {
          selectedValue: radio.value 
        };

        const url = 'http://127.0.0.1:8000/seller/product-manager/create/getradio';


        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
          },
          body: JSON.stringify(sendData) 
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log(data);
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
        });
      }
    });
  });
}


