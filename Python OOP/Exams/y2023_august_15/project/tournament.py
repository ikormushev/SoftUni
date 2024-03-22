from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        ElbowPad.__name__: lambda: ElbowPad(),
        KneePad.__name__: lambda: KneePad()
    }

    VALID_TEAMS = {
        OutdoorTeam.__name__: lambda x, y, z: OutdoorTeam(x, y, z),
        IndoorTeam.__name__: lambda x, y, z: IndoorTeam(x, y, z)
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise ValueError("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_list = [x for x in self.teams if x.name == team_name]
        wanted_equipment_list = [x for x in self.equipment if x.__class__.__name__ == equipment_type]
        if team_list and wanted_equipment_list:
            team = team_list[0]
            wanted_equipment = wanted_equipment_list[-1]

            if team.budget < wanted_equipment.price:
                raise Exception("Budget is not enough!")
            self.equipment.remove(wanted_equipment)
            team.equipment.append(wanted_equipment)
            team.budget -= wanted_equipment.price
            return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_list = [x for x in self.teams if x.name == team_name]
        if not team_list:
            raise Exception("No such team!")

        team = team_list[0]
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        total_changed = 0

        for eq in self.equipment:
            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                total_changed += 1

        return f"Successfully changed {total_changed}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = [x for x in self.teams if x.name == team_name1]
        second_team = [x for x in self.teams if x.name == team_name2]
        if first_team and second_team:
            first_team = first_team[0]
            second_team = second_team[0]
            if first_team.__class__.__name__ != second_team.__class__.__name__:
                raise Exception("Game cannot start! Team types mismatch!")

            first_team_points_sum = first_team.advantage + sum([x.protection for x in first_team.equipment])
            second_team_points_sum = second_team.advantage + sum([x.protection for x in second_team.equipment])

            if first_team_points_sum == second_team_points_sum:
                return "No winner in this game."
            elif first_team_points_sum > second_team_points_sum:
                first_team.win()
                return f"The winner is {first_team.name}."
            elif first_team_points_sum < second_team_points_sum:
                second_team.win()
                return f"The winner is {second_team.name}."

    def get_statistics(self):
        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"
        sorted_wins = sorted(self.teams, key=lambda x: -x.wins)
        if sorted_wins:
            result += "\n" + "\n".join([x.get_statistics() for x in sorted_wins])
        return result
