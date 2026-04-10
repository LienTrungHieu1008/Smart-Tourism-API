const input = document.getElementById('searchInput');
const btn = document.getElementById('searchBtn');
const resultsDiv = document.getElementById('results');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');

async function search() {
    const query = input.value.trim();
    if (!query) return;

    resultsDiv.innerHTML = '';
    errorDiv.style.display = 'none';
    loadingDiv.style.display = 'flex';

    try {
        const res = await fetch('/suggest', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query, top_k: 5 })
        });

        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || 'Có lỗi xảy ra');
        }

        const data = await res.json();
        renderResults(data);
    } catch (e) {
        errorDiv.textContent = e.message;
        errorDiv.style.display = 'block';
    } finally {
        loadingDiv.style.display = 'none';
    }
}

function renderResults(items) {
    resultsDiv.innerHTML = items.map(item => `
        <div class="card">
            <div class="card-header">
                <span class="card-name">📍 ${item.name}</span>
                <span class="card-score">${(item.score * 100).toFixed(1)}%</span>
            </div>
            <p class="card-desc">${item.description}</p>
        </div>
    `).join('');
}

btn.addEventListener('click', search);
input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') search();
});
