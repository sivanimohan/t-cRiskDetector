const terms = document.body.innerText;
chrome.runtime.sendMessage({ action: "analyze", data: terms });
