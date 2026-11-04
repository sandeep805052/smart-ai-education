const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");
    messageDiv.className = "message " + sender;

    if (sender === "bot") {
        const avatar = document.createElement("div");
        avatar.className = "avatar";
        avatar.textContent = "🤖";
        messageDiv.appendChild(avatar);
    }

    const content = document.createElement("div");
    content.className = "message-content";

    // Safely display text without interpreting HTML
    content.textContent = message;

    messageDiv.appendChild(content);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const message = userInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    userInput.value = "";

    sendBtn.disabled = true;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.response || "Something went wrong.");
        }

        addMessage(data.response, "bot");

    } catch (error) {

        addMessage(
            "Unable to connect to the chatbot. Please try again.",
            "bot"
        );

    } finally {

        sendBtn.disabled = false;
        userInput.focus();

    }
}


sendBtn.addEventListener("click", sendMessage);

userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


document.querySelectorAll(".quick-btn").forEach(button => {

    button.addEventListener("click", function() {

        userInput.value = this.textContent.trim();

        sendMessage();

    });

});


clearBtn.addEventListener("click", function() {

    chatBox.innerHTML = "";

    addMessage(
        "Hello! Welcome to AI Basics Chatbot. Ask me anything about AI!",
        "bot"
    );

});