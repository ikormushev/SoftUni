from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS_MONEY_FOR_PLACEMENT = {
        "Oracle": {
            1: 1500000,
            2: 800000
        },
        "Honda": {
            8: 20000,
            10: 10000
        }
    }
    TEAM_EXPENSES = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.TEAM_EXPENSES
        for (sponsor, placements) in self.SPONSORS_MONEY_FOR_PLACEMENT.items():
            possible_prize_placements = [x for x in range(1, 11) if x >= race_pos]
            for place in placements:
                if place in possible_prize_placements:
                    revenue += self.SPONSORS_MONEY_FOR_PLACEMENT[sponsor][place]
                    break

        self.budget += revenue
        return (f"The revenue after the race is {revenue}$. "
                f"Current budget {self.budget}$")
