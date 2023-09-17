export function sendSelectedValueToServer(selectedValue) {
  const url = 'http://127.0.0.1:8000/seller/product-manager/create/getcategory';
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
