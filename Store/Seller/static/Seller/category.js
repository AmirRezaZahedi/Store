const my_arr = [
  {
      "product": [
          {"digital": ["mobile", "TV"]},
          "clothes",
          {"drink": ["water", "wine", "soda"]}
      ]
  }
];

const treeContainer = document.getElementById("tree");

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

createTree(my_arr, treeContainer);