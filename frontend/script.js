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
            const response = await fetch(`${API_URL}?number=${number}`);
            const data = await response.json();

            // Hide loading spinner
            loadingSpinner.classList.add('hidden');

            if (response.ok) {
                const resultHTML = `
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                    <div>
                        <h3>Number Properties:</h3>
                        <p>🔢 Number: ${data.number}</p>
                        <p>🏁 Is Prime: ${data.is_prime ? '✅ Yes' : '❌ No'}</p>
                        <p>🌟 Is Perfect: ${data.is_perfect ? '✅ Yes' : '❌ No'}</p>
                        <p>🏷️ Properties: ${data.properties.join(', ')}</p>
                        <p>➕ Digit Sum: ${data.digit_sum}</p>
                        <p>💡 Fun Fact: ${data.fun_fact}</p>
                    </div>
                `;
                resultContent.innerHTML = resultHTML;
            } else {
                resultContent.innerHTML = `<p style="color: red;">${data.message || 'An error occurred'}</p>`;
            }
        } catch (error) {
            // Hide loading spinner
            loadingSpinner.classList.add('hidden');
            
            resultContent.innerHTML = `
                <p style="color: red;">
                    Unable to fetch data. Please check your internet connection.
                </p>
            `;
            console.error('Error:', error);
        }
    });

    // Optional: Add Enter key support
    numberInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            classifyBtn.click();
        }
    });
});
