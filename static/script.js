function encryptText() {
    const inputText = document.getElementById('inputText').value;

    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputText').value = data.encrypted_text;
    })
    .catch(error => console.error('Error:', error));
}

function decryptText() {
    const encryptedText = document.getElementById('encryptedText').value;

    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: encryptedText }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('decryptedText').value = data.decrypted_text;
    })
    .catch(error => console.error('Error:', error));
}
