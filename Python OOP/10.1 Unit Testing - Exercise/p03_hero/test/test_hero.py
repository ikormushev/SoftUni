import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Hero123", 1, 100, 100)

    def test_hero_initialization(self):
        self.assertEqual("Hero123", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_method_draw_outcome_both_zero_health(self):
        enemy = Hero("Enemy123", 1, 100, 100)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle_method_draw_outcome_both_negative_health(self):
        new_hero = Hero("New Hero", 1, 100, 200)
        enemy = Hero("Enemy123", 1, 100, 200)

        result = new_hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-100, new_hero.health)
        self.assertEqual(-100, enemy.health)

    def test_battle_method_draw_outcome_enemy_negative_health_hero_zero_health(self):
        new_hero = Hero("New Hero", 1, 100, 350)
        enemy = Hero("Enemy123", 1, 100, 200)

        result = new_hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-100, new_hero.health)
        self.assertEqual(-250, enemy.health)

    def test_battle_method_draw_outcome_hero_negative_health_enemy_zero_health(self):
        enemy = Hero("Enemy123", 1, 100, 300)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-200, self.hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle_method_win_outcome_enemy_zero_health(self):
        enemy = Hero("Enemy123", 1, 100, 15)
        result = self.hero.battle(enemy)
        self.assertEqual(0, enemy.health)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(90, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_win_outcome_enemy_negative_health(self):
        new_hero = Hero("New Hero", 1, 100, 345)
        enemy = Hero("Enemy123", 1, 100, 15)
        result = new_hero.battle(enemy)
        self.assertEqual(-245, enemy.health)

        self.assertEqual(2, new_hero.level)
        self.assertEqual(90, new_hero.health)
        self.assertEqual(350, new_hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_lose_outcome(self):
        enemy = Hero("Enemy123", 1, 200, 15)
        result = self.hero.battle(enemy)
        self.assertEqual(85, self.hero.health)

        self.assertEqual(2, enemy.level)
        self.assertEqual(105, enemy.health)
        self.assertEqual(20, enemy.damage)
        self.assertEqual("You lose", result)

    def test_battle_method_same_username_exception(self):
        enemy = Hero("Hero123", 1, 100, 25)
        result = None
        with self.assertRaises(Exception) as ex:
            result = self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))
        self.assertIsNone(result)

        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(100, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_battle_method_hero_negative_health(self):
        new_hero = Hero("Hero1", 1, -100, 45)
        enemy = Hero("Enemy123", 1, 100, 25)
        result = None
        with self.assertRaises(ValueError) as ex:
            result = new_hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        self.assertIsNone(result)

        self.assertEqual(1, new_hero.level)
        self.assertEqual(-100, new_hero.health)
        self.assertEqual(45, new_hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(100, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_battle_method_hero_zero_health(self):
        new_hero = Hero("Hero1", 1, 0, 45)
        enemy = Hero("Enemy123", 1, 100, 25)
        result = None
        with self.assertRaises(ValueError) as ex:
            result = new_hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        self.assertIsNone(result)

        self.assertEqual(1, new_hero.level)
        self.assertEqual(0, new_hero.health)
        self.assertEqual(45, new_hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(100, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_battle_method_enemy_negative_health(self):
        enemy = Hero("Enemy123", 1, 0, 25)
        result = None
        with self.assertRaises(ValueError) as ex:
            result = self.hero.battle(enemy)

        self.assertEqual("You cannot fight Enemy123. He needs to rest", str(ex.exception))
        self.assertIsNone(result)

        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(0, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_battle_method_enemy_zero_health(self):

        enemy = Hero("Enemy123", 1, -100, 25)
        result = None
        with self.assertRaises(ValueError) as ex:
            result = self.hero.battle(enemy)

        self.assertEqual("You cannot fight Enemy123. He needs to rest", str(ex.exception))
        self.assertIsNone(result)

        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

        self.assertEqual(1, enemy.level)
        self.assertEqual(-100, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_str_method(self):
        expected_result = f"Hero Hero123: 1 lvl\nHealth: 100\nDamage: 100\n"
        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    unittest.main()
