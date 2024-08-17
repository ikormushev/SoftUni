function attachEvents() {
    const submitButton = document.getElementById('submit');
    const locationsUrl = "http://localhost:3030/jsonstore/forecaster/locations";
    const currentForecastWeatherUrl = "http://localhost:3030/jsonstore/forecaster/today";
    const commingForecastWeatherUrl = "http://localhost:3030/jsonstore/forecaster/upcoming";

    submitButton.addEventListener('click', () => {
        let inputLocationTextValue = document.getElementById('location').value;
        let forecastDiv = document.getElementById('forecast');
        forecastDiv.style.display = 'block';
        let locationCode = "";
    
        async function getWeather() {
            try {
                let response = await fetch(locationsUrl);

                if (!response.ok) {
                    throw new Error();
                }

                let data = await response.json();
                data.forEach(location => 
                    {
                        if (location.name.toLowerCase() === inputLocationTextValue.toLowerCase()) {
                            locationCode = location.code;
                        }
                });


                let responseCurr = await fetch(`${currentForecastWeatherUrl}/${locationCode}`);

                if (!responseCurr.ok) {
                    throw new Error();
                }

                let dataCurr = await responseCurr.json();

                let responseComming = await fetch(`${commingForecastWeatherUrl}/${locationCode}`);

                if (!responseCurr.ok) {
                    throw new Error();
                }

                let dataComming = await responseComming.json();

                forecastDiv.style.display = "block";
                displayWeather(dataCurr, dataComming);

            } catch (error) {
                forecastDiv.textContent = "Error";
            }
        }

        getWeather();
    
        function displayWeather(todayData, upcomingData) {
            let currentConditionsDiv = document.getElementById('current');

            let currForecastsDiv = document.createElement('div');
            currForecastsDiv.classList.add('forecasts');
            currentConditionsDiv.appendChild(currForecastsDiv);
    
            let conditionSymbolSpan = document.createElement('span');
            conditionSymbolSpan.classList.add('condition');
            conditionSymbolSpan.classList.add('symbol');
            conditionSymbolSpan.textContent = getWeatherSymbol(todayData.forecast.condition);

            let mainConditionSpan = document.createElement('span');
            mainConditionSpan.classList.add('condition');

            let cityNameSpan = document.createElement('span');
            cityNameSpan.classList.add('forecast-data');
            cityNameSpan.textContent = todayData.name;

            let temperaturesCondition = document.createElement('span');
            temperaturesCondition.classList.add('forecast-data');
            temperaturesCondition.textContent = `${todayData.forecast.low}°/${todayData.forecast.high}°`;

            let conditionSpan = document.createElement('span');
            conditionSpan.classList.add('forecast-data');
            conditionSpan.textContent = todayData.forecast.condition;
            
            // Append all to the father element
            currForecastsDiv.appendChild(conditionSymbolSpan);
            currForecastsDiv.appendChild(mainConditionSpan);
            
            mainConditionSpan.appendChild(cityNameSpan);
            mainConditionSpan.appendChild(temperaturesCondition);
            mainConditionSpan.appendChild(conditionSpan);


            // Upcoming Days
            let upcomingConditionsDiv = document.getElementById('upcoming');
            let forecastInfoDiv = document.createElement('div');
            forecastInfoDiv.classList.add('forecast-info');
            upcomingConditionsDiv.appendChild(forecastInfoDiv);

            for (let newForecast of upcomingData.forecast) {
                let upcomingSpan = document.createElement('span');
                upcomingSpan.classList.add('upcoming');

                let symbolSpan = document.createElement('span');
                symbolSpan.classList.add('symbol');
                symbolSpan.textContent = getWeatherSymbol(newForecast.condition);
    
                let temperaturesCondition = document.createElement('span');
                temperaturesCondition.classList.add('forecast-data');
                temperaturesCondition.textContent = `${newForecast.low}°/${newForecast.high}°`;
    
                let conditionSpan = document.createElement('span');
                conditionSpan.classList.add('forecast-data');
                conditionSpan.textContent = newForecast.condition;
                
                // Append all to the father element
                upcomingSpan.appendChild(symbolSpan);
                upcomingSpan.appendChild(temperaturesCondition);
                upcomingSpan.appendChild(conditionSpan);

                forecastInfoDiv.appendChild(upcomingSpan);
            }
        }

        function getWeatherSymbol(condition) {
            switch (condition) {
                case 'Sunny': return '☀'; // &#x2600;
                case 'Partly sunny': return '⛅'; // &#x26C5;
                case 'Overcast': return '☁'; // &#x2601;
                case 'Rain': return '☂'; // &#x2614;
                default: return '';
            }
        }
    });
}

attachEvents();
