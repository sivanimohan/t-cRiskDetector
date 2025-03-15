document.getElementById('analyzeButton').addEventListener('click', async () => {
  const text = document.getElementById('inputText').value;

  if (!text) {
    alert('Please enter some text');
    return;
  }

  const response = await fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text }),
  });

  const result = await response.json();
  document.getElementById('result').innerText = `Risk: ${result.risk} (${result.confidence.toFixed(2)}%)`;
});
