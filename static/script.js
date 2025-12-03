// Configuration
const API_BASE_URL = 'http://localhost:8000';

// Switch between tabs
function switchTab(tabName) {
    // Hide all tab contents
    const contents = document.querySelectorAll('.avatar-content');
    contents.forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.avatar-tab-btn');
    buttons.forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab content
    const selectedContent = document.getElementById(tabName);
    if (selectedContent) {
        selectedContent.classList.add('active');
    }

    // Add active class to clicked button
    event.target.closest('.avatar-tab-btn').classList.add('active');
}

// Call API
async function callApi(endpoint, method) {
    const x = parseFloat(document.getElementById(`${endpoint}_x`).value);
    const y = parseFloat(document.getElementById(`${endpoint}_y`).value);
    const resultBox = document.getElementById(`${endpoint}_result`);

    // Validate input
    if (isNaN(x) || isNaN(y)) {
        resultBox.innerHTML = '❌ Пожалуйста, введите корректные числа';
        resultBox.className = 'avatar-result error';
        return;
    }

    // Show loading state
    resultBox.innerHTML = '<span class="spinner"></span>Загрузка...';
    resultBox.className = 'avatar-result loading';

    try {
        let response;
        let url = `${API_BASE_URL}/${endpoint}`;

        if (method === 'GET') {
            url += `?x=${x}&y=${y}`;
            response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });
        } else {
            response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ x: x, y: y })
            });
        }

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Display result
        resultBox.innerHTML = `
            <div style="text-align: center; width: 100%; color: inherit;">
                <p style="font-size: 1.2em;"><strong>✨ Результат: </strong><span style="color: #00ff00; font-weight: bold;">${data.result}</span></p>
            </div>
        `;
        resultBox.className = 'avatar-result success';
    } catch (error) {
        resultBox.innerHTML = `❌ Ошибка: ${error.message}. Убедитесь, что API запущен на ${API_BASE_URL}`;
        resultBox.className = 'avatar-result error';
        console.error('API Error:', error);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Frontend loaded successfully');
    console.log('API Base URL:', API_BASE_URL);
});
