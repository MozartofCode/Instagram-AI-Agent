// popup.js

document.getElementById('sendDataButton').addEventListener('click', () => {
    console.log("Button clicked");

    const data = {
        prompt: ''
    };

    fetch('http://127.0.0.1:5000/process-prompt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        console.log("Click Received")
        return response.json()})
            
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});