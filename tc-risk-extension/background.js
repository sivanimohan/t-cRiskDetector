chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "analyze") {
    fetch("https://t-criskdetector.onrender.com", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: request.data })
    })
      .then(response => response.json())
      .then(data => {
        chrome.runtime.sendMessage({ action: "result", result: data });
      });
  }
});
