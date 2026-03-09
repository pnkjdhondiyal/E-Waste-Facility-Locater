// Initialize map
const map = L.map('map').setView([28.6139, 77.2090], 12); // Default: Delhi

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Custom icon for recycling centers
const recycleIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

let userLocation = null;

// Fetch facilities from backend
fetch('/api/facilities/')
    .then(response => response.json())
    .then(facilities => {
        if (facilities.length === 0) {
            document.getElementById('facilities-content').innerHTML = '<p>No facilities found. Add some via admin panel.</p>';
            return;
        }
        
        facilities.forEach(facility => {
            const marker = L.marker([facility.latitude, facility.longitude], {icon: recycleIcon})
                .addTo(map);
            
            const popupContent = `
                <b>${facility.name}</b><br>
                ${facility.address}<br>
                ${facility.phone ? `📞 ${facility.phone}<br>` : ''}
                ${facility.email ? `📧 ${facility.email}` : ''}
            `;
            
            marker.bindPopup(popupContent);
        });
        
        // Display facilities list
        displayFacilitiesList(facilities);
        
        // Fit map to show all markers
        const bounds = L.latLngBounds(facilities.map(f => [f.latitude, f.longitude]));
        map.fitBounds(bounds, {padding: [50, 50]});
    })
    .catch(error => console.error('Error loading facilities:', error));

function displayFacilitiesList(facilities) {
    // Sort facilities by distance if user location is available
    let sortedFacilities = [...facilities];
    
    if (userLocation) {
        sortedFacilities = sortedFacilities.map(facility => {
            const dist = calculateDistance(
                userLocation.lat, userLocation.lng,
                facility.latitude, facility.longitude
            );
            return { ...facility, distance: dist };
        }).sort((a, b) => a.distance - b.distance);
    }
    
    const content = sortedFacilities.map((facility, index) => {
        let distance = '';
        if (userLocation && facility.distance !== undefined) {
            distance = `<p><strong>📍 ${facility.distance.toFixed(1)} km away</strong></p>`;
        }
        
        return `
            <div class="facility-item" style="${index === 0 && userLocation ? 'border-left-color: #27ae60; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);' : ''}">
                ${index === 0 && userLocation ? '<span style="color: #27ae60; font-weight: bold; font-size: 0.85rem;">🎯 NEAREST</span>' : ''}
                <h4>${facility.name}</h4>
                <p>📍 ${facility.address}</p>
                ${distance}
                ${facility.phone ? `<p>📞 ${facility.phone}</p>` : ''}
                ${facility.email ? `<p>📧 ${facility.email}</p>` : ''}
            </div>
        `;
    }).join('');
    
    document.getElementById('facilities-content').innerHTML = content;
}

function calculateDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Earth radius in km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLon/2) * Math.sin(dLon/2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    return R * c;
}

// Get user location
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
        userLocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        
        L.marker([userLocation.lat, userLocation.lng])
            .addTo(map)
            .bindPopup('📍 You are here')
            .openPopup();
        
        map.setView([userLocation.lat, userLocation.lng], 13);
        
        // Reload facilities list with distances and sorting
        fetch('/api/facilities/')
            .then(response => response.json())
            .then(facilities => {
                displayFacilitiesList(facilities);
            });
    });
}
