const treeContainer = document.getElementById("tree");

function getcategory() {
    const url = 'http://127.0.0.1:8000/product-manager/create/getcategory';

    
    fetch(url)
      .then(response => {
        
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log(response);
        return response.json();
      })
      .then(data => {
        createTree(data, treeContainer)
        //console.log(data);
      })
      .catch(error => {
        
        console.error('There was a problem with the fetch operation:', error);
      });


}
const my_arr = [
  {
      "product": [
          {"digital": ["mobile", "TV"]},
          "clothes",
          {"drink": ["water", "wine", "soda"]}
      ]
  }
];



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

      } 
      else {

          key = Object.keys(data)[0];
          
          sublist.textContent = key;
          const subitem = document.createElement("ul");
                        
          createTree(data[key], subitem);
                  
          sublist.appendChild(subitem);
          parent.appendChild(sublist);
                  
      }
  }
}

//createTree(my_arr, treeContainer);