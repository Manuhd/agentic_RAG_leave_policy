let chatHistory = [];
const chatBox = document.getElementById("chat-box");

/* ================= LOGIN ================= */

function login() {
  const userId = document.getElementById("userId").value;
  const password = document.getElementById("password").value;

  if (!userId || !password) {
    alert("Enter ID and password");
    return;
  }

  // demo login
  localStorage.setItem("user_id", String(userId));
  window.location.href = "chat.html";
}

function logout() {
  localStorage.clear();
  window.location.href = "index.html";
}

// Protect chat page
if (window.location.pathname.includes("chat.html")) {
  if (!localStorage.getItem("user_id")) {
    window.location.href = "index.html";
  }
}

/* ================= CHAT ================= */

function addMessage(text, sender) {
  if (!chatBox) return;

  const msg = document.createElement("div");
  msg.className = `message ${sender}`;
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("messageInput");
  const message = input.value.trim();
  if (!message) return;

  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("User not logged in");
    return;
  }

  addMessage(message, "user");
  chatHistory.push(`Q: ${message}`);
  input.value = "";

  const payload = {
    question: message,
    user_id: String(userId),
    chat_history: chatHistory
  };

  const response = await fetch("http://127.0.0.1:8000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const err = await response.text();
    console.error("Backend error:", err);
    alert("Request failed");
    return;
  }

  const data = await response.json();
  addMessage(data.answer, "bot");
  chatHistory.push(`A: ${data.answer}`);
}
