function solve() {
    let currentStop = {
        name: '',
        next: 'depot'
    };

    const infoBox = document.querySelector('.info');
    const departBtn = document.getElementById('depart');
    const arriveBtn = document.getElementById('arrive');

    function depart() {
        fetch(`http://localhost:3030/jsonstore/bus/schedule/${currentStop.next}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Could not fetch data');
            }
            return response.json();
        })
        .then(data => {
            currentStop.name = data.name;
            currentStop.next = data.next;

            infoBox.textContent = `Next stop ${currentStop.name}`;
            
            departBtn.disabled = true;
            arriveBtn.disabled = false;
        })
        .catch(() => {
            infoBox.textContent = 'Error';
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        });
    }

    async function arrive() {
        try {
            infoBox.textContent = `Arriving at ${currentStop.name}`;
            
            departBtn.disabled = false;
            arriveBtn.disabled = true;
        } catch (error) {
            infoBox.textContent = 'Error';
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
