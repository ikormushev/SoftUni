import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, F, Sum, Avg


# Django Queries I
def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    if search_string == "":
        query = Q()
    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts:
        return ""

    return "\n".join(f"Astronaut: {a.name}, "
                     f"phone number: {a.phone_number}, "
                     f"status: {'Active' if a.is_active else 'Inactive'}"
                     for a in astronauts)


def get_top_astronaut():
    top_astronaut = (Astronaut.objects
                     .annotate(missions_count=Count('mission_astronauts'))
                     .filter(missions_count__gt=0)
                     .order_by('-missions_count', 'phone_number')
                     .first())

    if not top_astronaut:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


def get_top_commander():
    top_astronaut = (Astronaut.objects
                     .annotate(missions_commanded=Count('mission_commander'))
                     .filter(missions_commanded__gt=0)
                     .order_by('-missions_commanded', 'phone_number')
                     .first())

    if not top_astronaut:
        return "No data."

    return f"Top Commander: {top_astronaut.name} with {top_astronaut.missions_commanded} commanded missions."


# Django Queries II
def get_last_completed_mission():
    last_completed_mission = (Mission.objects
                              .filter(status='Completed')
                              .order_by('-launch_date').first())

    if not last_completed_mission:
        return "No data."

    astronauts = ", ".join(a.name for a in last_completed_mission.astronauts.order_by('name'))
    commander_name = last_completed_mission.commander.name \
        if last_completed_mission.commander is not None \
        else "TBA"
    total_spacewalks = sum([a.spacewalks for a in last_completed_mission.astronauts.all()])

    return (f"The last completed mission is: {last_completed_mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts}. "
            f"Spacecraft: {last_completed_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    most_used_spacecraft = (Spacecraft.objects
                            .prefetch_related('mission_spacecraft')
                            .annotate(missions_count=Count('mission_spacecraft', distinct=True)
                                      , astronauts_count=Count('mission_spacecraft__astronauts', distinct=True))
                            .filter(missions_count__gt=0)
                            .order_by('-missions_count', 'name')
                            .first())

    if not most_used_spacecraft:
        return "No data."

    return (f"The most used spacecraft is: {most_used_spacecraft.name}, "
            f"manufactured by {most_used_spacecraft.manufacturer}, "
            f"used in {most_used_spacecraft.missions_count} missions, "
            f"astronauts on missions: {most_used_spacecraft.astronauts_count}.")


def decrease_spacecrafts_weight():
    spacecrafts_to_update = (Spacecraft.objects
                             .prefetch_related('mission_spacecraft')
                             .filter(mission_spacecraft__status='Planned', weight__gte=200.0)
                             .distinct())

    if not spacecrafts_to_update:
        return "No changes in weight."

    updated_spacecrafts_count = spacecrafts_to_update.update(weight=F('weight') - 200)
    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {updated_spacecrafts_count} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
