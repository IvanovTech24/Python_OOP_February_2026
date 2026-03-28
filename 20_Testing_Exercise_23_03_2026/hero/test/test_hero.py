from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = "Test Hero"
    level = 7
    health = 34.5
    damage = 24.3

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)


    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)


    def test_enemy_hero_same_names(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))


    def test_health_hero_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = -1
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))



    def test_health_enemy_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as vae:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(vae.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as vae2:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(vae2.exception))



    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-135.6, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)


    def test_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(38.5, self.hero.health)
        self.assertEqual(29.3, self.hero.damage)


    def test_hero_lose(self):
        enemy = Hero("Enemy", 100, 100, 100)
        self.hero.health = 10
        self.hero.damage = 10

        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(35, enemy.health)
        self.assertEqual(105, enemy.damage)


    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    main()