/*const radioButtons = document.querySelectorAll(".radio-button");

radioButtons.forEach(radio => {
  radio.addEventListener("click", function() {
    if (radio.checked) {
      
      const sendData = {
        selectedValue: radio.value 
      };
      

      const url = 'http://127.0.0.1:8000/seller/product-manager/create/getradio';


      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
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
*/