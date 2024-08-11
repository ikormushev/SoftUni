async function getCountry() {
    try {
        let response = await fetch('https://restcountries.com/v2/name/Bulgaria');
        let countryData = await response.json();
        console.log(JSON.stringify(countryData, null, 2));
    } catch(error) {
        console.error('Error fetching country data', error);
    }
}

getCountry();
