document.getElementById("weatherForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const city = document.getElementById("cityInput").value;

    const response = await fetch("/weather", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city })
    });

    const result = await response.json();
    const weatherDiv = document.getElementById("weatherResult");

    if(response.ok){
        weatherDiv.innerHTML = `
            <h2>${result.city}</h2>
            <p>${result.description}</p>
            <h3>${result.temperature} °C</h3>
            <img src="http://openweathermap.org/img/wn/${result.icon}@2x.png" alt="weather icon">
        `;
    } else {
        weatherDiv.innerHTML = `<p class="text-danger">${result.error}</p>`;
    }

    return false; // prevents any default submission
});