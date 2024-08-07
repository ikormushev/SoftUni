function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   let input = document.querySelector('#inputs textarea');

   let bestRestaurantOutputEl = document.querySelector('#outputs #bestRestaurant p');
   let bestWorkersOutputEl = document.querySelector('#outputs #workers p');

   function onClick () {
      let restaurants = [];
      let matches = JSON.parse(input.value);
   
      for (let info of matches) {
         let [restaurantName, workersInfo] = info.split(' - ');
         let filteredRestaurants = restaurants.filter(x => x.name === restaurantName);

         let newRestaurant = {};
         if (filteredRestaurants.length === 0) {
            newRestaurant.name = restaurantName;
            newRestaurant.workers = [];
         } else {
            newRestaurant = filteredRestaurants[0];
         }

         let workers = workersInfo.split(", ");
         for (let worker of workers) {
            let [workerName, salary] = worker.split(" ");
            salary = Number(salary);
            let workerObj = {name: workerName, salary: salary};

            newRestaurant.workers.push(workerObj);
         }
         restaurants.push(newRestaurant);
      }

      for (let restaurant of restaurants) {
         restaurant.workers = restaurant.workers.sort((x, y) => y.salary - x.salary);
         restaurant.averageSalary = restaurant.workers.reduce((acc, curr) => acc + curr.salary, 0) / restaurant.workers.length;
         restaurant.bestSalary = restaurant.workers[0].salary;
      }

      restaurants.sort((x, y) => y.averageSalary - x.averageSalary);
      let bestRestaurant = restaurants[0];
   
      if (bestRestaurant !== null) {
         bestRestaurantOutputEl.textContent = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.averageSalary.toFixed(2)} Best Salary: ${bestRestaurant.bestSalary.toFixed(2)}`;
         bestWorkersOutputEl.textContent = bestRestaurant.workers.map(x => `Name: ${x.name} With Salary: ${x.salary}`).join(" ");
      }

   }
}
