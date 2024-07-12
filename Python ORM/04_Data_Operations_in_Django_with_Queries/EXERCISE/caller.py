import os
import django
from _decimal import Decimal

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
# Task 1
def create_pet(name: str, species: str):
    new_pet = Pet(name=name, species=species)
    new_pet.save()

    return f"{new_pet.name} is a very cute {new_pet.species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


# Task 2
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    new_artifact = Artifact.objects.create(name=name,
                                           origin=origin,
                                           age=age,
                                           description=description,
                                           is_magical=is_magical)
    return f"The artifact {new_artifact.name} is {new_artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    artifacts = Artifact.objects.all()
    artifacts.delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom',
#                       500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)

# Task 3
def show_all_locations():
    locations = Location.objects.all().order_by("-id")
    result = []

    for loc in locations:
        result.append(f"{loc.name} has a population of {loc.population}!\n")

    return "".join(result)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    location = Location.objects.first()
    location.delete()


# Task 4
def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount_price = sum(int(num) for num in str(car.year))
        car.price_with_discount = float(car.price) * (1 - (discount_price / 100))
        # the car.price has to be a float, otherwise an error occurs
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values("model", "price_with_discount")


def delete_last_car():
    car = Car.objects.last()
    car.delete()


# Task 5
def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)
    result = [f"Task - {task.title} needs to be done until {task.due_date}!\n" for task in tasks]
    return "".join(result)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    new_text = "".join(chr(ord(sym) - 3) for sym in text)
    Task.objects.filter(title=task_title).update(description=new_text)


# Task 6
def get_deluxe_rooms():
    rooms = HotelRoom.objects.all()
    result = []

    for room in rooms:
        if room.room_type == "Deluxe" and room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} "
                          f"costs {room.price_per_night}$ per night!")
    return "\n".join(result)


def increase_room_capacity():
    rooms = HotelRoom.objects.filter(is_reserved=True).order_by("id")

    prev_capacity = 0

    for room in rooms:
        if prev_capacity == 0:
            room.capacity += room.id
        else:
            room.capacity += prev_capacity

        prev_capacity = room.capacity
        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    if not room.is_reserved:
        room.is_reserved = True
        room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()


# Task 7
def update_characters():
    characters = Character.objects.all()

    for cha in characters:
        if cha.class_name == "Mage":
            cha.level += 3
            cha.intelligence -= 7
        elif cha.class_name == "Warrior":
            cha.hit_points //= 2
            cha.dexterity += 4
        else:
            cha.inventory = "The inventory in empty"

    Character.objects.bulk_update(characters, ["level", "intelligence", "hit_points", "dexterity", "inventory"])


def fuse_characters(first_character: Character, second_character: Character):
    new_character = Character(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=((first_character.level + second_character.level) // 2),
        strength=((first_character.strength + second_character.strength) * 1.2),
        dexterity=((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory="Bow of the Elven Lords, "
                  "Amulet of Eternal Wisdom"
        if first_character.class_name in ["Mage", "Scout"]
        else "Dragon Scale Armor, Excalibur"
    )

    new_character.save()
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    characters = Character.objects.all()

    for cha in characters:
        cha.dexterity = 30

    Character.objects.bulk_update(characters, ["dexterity"])


def grand_intelligence():
    characters = Character.objects.all()

    for cha in characters:
        cha.intelligence = 40

    Character.objects.bulk_update(characters, ["intelligence"])


def grand_strength():
    characters = Character.objects.all()

    for cha in characters:
        cha.strength = 50

    Character.objects.bulk_update(characters, ["strength"])


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()
