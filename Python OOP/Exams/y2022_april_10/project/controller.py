class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        successful_players_additions = []
        for player in players:
            try:
                existing_player = next(filter(lambda p: p.name == player.name, self.players))
            except StopIteration:
                self.players.append(player)
                successful_players_additions.append(player.name)
        return f"Successfully added: {', '.join(successful_players_additions)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            needed_sustenance = None
            try:
                needed_sustenance = next(filter(lambda s: s.__class__.__name__ == sustenance_type, self.supplies[::-1]))
                if player.stamina + needed_sustenance.energy > player.MAX_STAMINA:
                    player.stamina = player.MAX_STAMINA
                else:
                    player.stamina += needed_sustenance.energy
                self.supplies.reverse()
                self.supplies.remove(needed_sustenance)
                self.supplies.reverse()
                return f"{player_name} sustained successfully with {needed_sustenance.name}."

            except StopIteration:
                if sustenance_type in self.VALID_SUSTENANCE_TYPES:
                    raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        except StopIteration:
            pass

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = player = next(filter(lambda p: p.name == first_player_name, self.players))
        second_player = player = next(filter(lambda p: p.name == second_player_name, self.players))

        zero_stamina_message = '\n'.join([f"Player {p.name} does not have enough stamina."
                                          for p in [first_player, second_player] if p.stamina == 0])
        if zero_stamina_message:
            return zero_stamina_message

        player_with_lower_stamina = first_player if first_player.stamina < second_player.stamina else second_player
        enemy = first_player if player_with_lower_stamina is second_player else second_player

        winner = None
        if enemy.stamina - (player_with_lower_stamina.stamina * 1/2) <= 0:
            enemy.stamina = 0
            return f"Winner: {player_with_lower_stamina.name}"
        elif player_with_lower_stamina.stamina - (enemy.stamina * 1/2) <= 0:
            player_with_lower_stamina.stamina = 0
            return f"Winner: {enemy.name}"

        enemy.stamina -= player_with_lower_stamina.stamina * 1 / 2
        player_with_lower_stamina.stamina -= enemy.stamina * 1 / 2
        winner = enemy if enemy.stamina > player_with_lower_stamina.stamina else player_with_lower_stamina
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join(str(p) for p in self.players) + "\n" + "\n".join(s.details() for s in self.supplies)
