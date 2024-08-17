function getInfo() {
    const linkStops = "http://localhost:3030/jsonstore/bus/businfo";
    const submitButton = document.getElementById("submit");

    let submitId = document.getElementById("stopId").value;
    let resultDiv = document.getElementById('stopName');
    let busesUl = document.getElementById('buses');
    busesUl.childNodes.forEach(x => x.remove());

    async function getAllStops() {
        try {
            let response = await fetch(`${linkStops}/${submitId}`);

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            let data = await response.json();
            resultDiv.textContent = data.name;

            let buses = Object.entries(data.buses);
            buses.forEach(bus => {
                let newLi = document.createElement('li');
                newLi.textContent = `Bus ${bus[0]} arrives in ${bus[1]} minutes`;
                busesUl.appendChild(newLi);
            });

        } catch (error) {
            resultDiv.textContent = "Error";
        }
    }

    getAllStops();
}
