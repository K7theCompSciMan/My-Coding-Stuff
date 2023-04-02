
const apiKey= "a61d2ee41192787c141ea0faddfe5949";
const apiUrl =" https://api.openweathermap.org/data/2.5/weather?";
const reset = document.querySelector(".reset");
const temp = document.querySelector(".temp");
const wind = document.querySelector(".wind-label");
const humidity = document.querySelector(".humidity-label");
const cityName = document.querySelector(".name");
const unit = document.querySelector(".unit");
const input = document.querySelector(".inputs input");
let units = "imperial";

async function getWeather(name) {
    const response = await fetch(apiUrl + `units=${units}`+ `&q=${name}` + `&appid=${apiKey}`);
    var data = await response.json();
    console.log(data);
    cityName.innerHTML = data.name;
    if(unit.innerHTML === "°F"){
        temp.innerHTML = Math.round(data.main.temp) + "°C";
        wind.innerHTML = data.wind.speed + "km/h";
    }
    else if(unit.innerHTML === "°C"){
        temp.innerHTML = Math.round(data.main.temp) + "°F";
        wind.innerHTML = data.wind.speed + "m/h";  
    }
    
    humidity.innerHTML = data.main.humidity + "%";
    document.querySelector(".icon img").src = `https://openweathermap.org/img/w/${data.weather[0].icon}.png`;
    document.querySelector(".icon img").alt = data.weather[0].description;
}
document.querySelector(".inputs button").addEventListener("click", () => {
    getWeather(input.value.toLowerCase());
})

input.addEventListener('keydown', (e)=>{
    if(e.code=="Enter"){
        if(input.value!=""){
            getWeather(input.value.toLowerCase());
        }
    }
})

unit.addEventListener("click", () => {
    if (unit.innerHTML == "°C"){
        unit.innerHTML = "°F";
        units = "metric";
        temp.innerHTML = "Temperature °C";
        wind.innerHTML = "Wind Speed (km/h)";
    }
    else if (unit.innerHTML == "°F"){
        unit.innerHTML = "°C";
        units = "imperial"
        temp.innerHTML = "Temperature °F";
        wind.innerHTML = "Wind Speed (m/h)";
    }
    if(input.value.toLowerCase() != ""){
        getWeather(input.value.toLowerCase());
    }
    
})
reset.addEventListener("click", () => {
    temp.innerHTML = "Temperature °F";
    cityName.innerHTML = "City Name";
    humidity.innerHTML = "Humidity %";
    wind.innerHTML = "Wind Speed (m/h)";
    unit.innerHTML = "°C";
    input.value = ""

})