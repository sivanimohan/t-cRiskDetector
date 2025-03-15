document.getElementById("analyze").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      files: ["content.js"]
    });
  });
});
chrome.runtime.onMessage.addListener((request) => {
  if (request.action === "result") {
    document.getElementById("result").innerText = 
      `Risk Level: ${request.result.risk} (${request.result.confidence}%)`;
  }
});
