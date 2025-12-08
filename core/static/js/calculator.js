document.getElementById('calculatorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const btn = document.getElementById('calculateBtn');
    const btnText = document.getElementById('btnText');
    const btnLoader = document.getElementById('btnLoader');
    
    btnText.style.display = 'none';
    btnLoader.style.display = 'inline';
    btn.disabled = true;
    
    const formData = new FormData(e.target);
    const data = {
        brand: formData.get('brand'),
        processor: formData.get('processor'),
        gpu: formData.get('gpu'),
        age: formData.get('age'),
        weight: formData.get('weight'),
        material: formData.get('material')
    };
    
    try {
        const response = await fetch('/calculator/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error('Server error');
        }
        
        const result = await response.json();
        
        if (result.error) {
            alert('Error: ' + result.error);
            return;
        }
        
        document.getElementById('estimatedValue').textContent = `$${result.estimated_value}`;
        document.getElementById('carbonSaved').textContent = `${result.carbon_saved} kg CO2`;
        document.getElementById('results').style.display = 'block';
        
        document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
        console.error('Error:', error);
        alert('Error calculating values. Please check all fields and try again.');
    } finally {
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
        btn.disabled = false;
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
