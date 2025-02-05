const API_URL = 'https://numbers-api-hng-12.vercel.app/api/classify-number';

document.addEventListener('DOMContentLoaded', () => {
    const numberInput = document.getElementById('numberInput');
    const classifyBtn = document.getElementById('classifyBtn');
    const resultContent = document.getElementById('resultContent');
    const loadingSpinner = document.getElementById('loadingSpinner');

    classifyBtn.addEventListener('click', async () => {
        const number = numberInput.value.trim();

        if (!number) {
            resultContent.innerHTML = '<p style="color: red;">Please enter a number</p>';
            return;
        }

        // Show loading spinner
        loadingSpinner.classList.remove('hidden');
        resultContent.innerHTML = '';

        try {
            console.log(`Fetching data from: ${API_URL}?number=${number}`);
            
            const response = await fetch(`${API_URL}?number=${number}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });

            console.log('Response status:', response.status);
            console.log('Response headers:', Object.fromEntries(response.headers.entries()));

            const data = await response.json();
            console.log('Parsed response data:', data);

            // Hide loading spinner
            loadingSpinner.classList.add('hidden');

            if (response.ok) {
                const resultHTML = `
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                    <div>
                        <h3>Number Properties:</h3>
                        <p> Number: ${data.number}</p>
                        <p> Is Prime: ${data.is_prime ? ' Yes' : ' No'}</p>
                        <p> Is Perfect: ${data.is_perfect ? ' Yes' : ' No'}</p>
                        <p> Properties: ${data.properties.join(', ')}</p>
                        <p> Digit Sum: ${data.digit_sum}</p>
                        <p> Fun Fact: ${data.fun_fact}</p>
                    </div>
                `;
                resultContent.innerHTML = resultHTML;
            } else {
                resultContent.innerHTML = `
                    <p style="color: red;">
                        API Error: ${data.message || 'Unknown error occurred'}
                        <br>Status: ${response.status}
                        <br>Details: ${JSON.stringify(data)}
                    </p>
                `;
            }
        } catch (error) {
            // Hide loading spinner
            loadingSpinner.classList.add('hidden');
            
            resultContent.innerHTML = `
                <p style="color: red;">
                    Network Error: Unable to fetch data.
                    <br>Error Details: ${error.message}
                    <br>API URL: ${API_URL}?number=${number}
                </p>
            `;
            console.error('Fetch Error:', error);
        }
    });

    // Optional: Add Enter key support
    numberInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            classifyBtn.click();
        }
    });
});
