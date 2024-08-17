function attachEvents() {
    const requestUrl = "http://localhost:3030/jsonstore/messenger";

    const messagesArea = document.getElementById('messages');
    const sendButton = document.getElementById('submit');
    const refreshButton = document.getElementById('refresh');

    const authorEl = document.querySelector('input[type="text"][name="author"]');
    const contentEl = document.querySelector('input[type="text"][name="content"]');

    sendButton.addEventListener('click', async () => {
        await fetch(requestUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({author: authorEl.value, content: contentEl.value}),
        })
    });

    refreshButton.addEventListener('click', async () => {
        let response = await fetch(requestUrl);
        let data = await response.json();
        let messages = Object.values(data);

        messagesArea.value = messages.map(message => `${message.author}: ${message.content}`).join("\n");
    });
}

attachEvents();
