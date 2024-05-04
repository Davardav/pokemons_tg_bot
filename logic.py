from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.hp = randint(100,300)
        self.power = randint(20,45)
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        if isinstance(self, Wizard):
            self.hp += randint(30,90)
        elif isinstance(self, Fighter):
            self.power += randint(7,12)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                next_url = (data['forms'][0]['url'])
                response = requests.get(next_url)
                if response.status_code == 200:
                    data = response.json()
                    return (data['sprites']['front_default'])
                
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chanse = randint(1,5)
            if chanse == 1:
                return "Покемон-волшебник применил щит в сражении"
        
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    # Метод класса для получения информации
    def info(self):
        pclass = ''
        if isinstance(self, Wizard):
            pclass = "У тебя покемон-волшебник"
        elif isinstance(self, Fighter):
            pclass = "У тебя покемон-Боец"
        return f"""Имя твоего покеомона: {self.name}
        атака покемона: {self.power}
        хп покемона: {self.hp}
        {pclass}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    def attack(self, enemy):
        return super().attack(enemy)

class Fighter (Pokemon):
    def attack(self, enemy):
        extra_power = randint(5,15)
        self.power += extra_power
        result = super().attack(enemy)
        self.power -= extra_power
        return result + f"\Боец применил супер-атаку силой:{extra_power + self.power} "

    