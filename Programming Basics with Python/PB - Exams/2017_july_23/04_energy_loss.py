N = int(input())  # training_days
A = int(input())  # dancers_num

energy = 100 * N * A
energy_loss = 0

for i in range(1, N + 1):
    training_hours = int(input())
    if (i % 2 == 0) and (training_hours % 2 == 0):
        energy_loss = A * 68
    elif (i % 2 == 1) and (training_hours % 2 == 0):
        energy_loss = A * 49
    elif (i % 2 == 0) and (training_hours % 2 == 1):
        energy_loss = A * 65
    else:
        energy_loss = A * 30
    energy -= energy_loss

energy_left = (energy / A) / N  # energy_left per dancer per day
average_energy_loss = (100 * N * A - energy) / A / N  # average_energy_loss == (100 - energy_left)

if average_energy_loss <= 50:
    print(f"They feel good! Energy left: {energy_left:.2f}")
elif average_energy_loss > 50:
    print(f"They are wasted! Energy left: {energy_left:.2f}")
