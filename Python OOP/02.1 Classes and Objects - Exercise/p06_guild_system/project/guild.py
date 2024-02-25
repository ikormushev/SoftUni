from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for searched_player in self.players:
            if searched_player.name == player_name:
                searched_player.guild = "Unaffiliated"
                self.players.remove(searched_player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join([x.player_info() for x in self.players])


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))
print(player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
