"""
Proyecto: Ejemplo corto de herencia en POO con equipos de fútbol.
- FootballTeam (clase base)
- ClubTeam (clase hija)
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class FootballTeam:
    """Clase base."""

    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.trophies = 0
        logging.info(f"Equipo creado: {self.name} ({self.country})")

    def win_trophy(self):
        self.trophies += 1
        print(f"{self.name} gana un trofeo. Total: {self.trophies}")


class ClubTeam(FootballTeam):
    """Clase hija: hereda atributos y métodos de FootballTeam."""

    def __init__(self, name: str, country: str, stadium: str):
        super().__init__(name, country)
        self.stadium = stadium

    def play_home(self):
        print(f"{self.name} juega en casa: {self.stadium}")


if __name__ == "__main__":
    real_madrid = ClubTeam("Real Madrid", "España", "Santiago Bernabéu")

    real_madrid.win_trophy()
    real_madrid.play_home()
