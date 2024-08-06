from person import Person
from address import Address
from datetime import date


class Teacher(Person):
    """
    Classe représentant un enseignant, héritant de la classe Person.
    """

    def __init__(self, name: str, surname: str, age: int, address: Address, phone: int, mail: str, arrival_date: date):
        """
        Initialise un nouvel enseignant.

        Args:
            name (str): Prénom de l'enseignant.
            surname (str): Nom de famille de l'enseignant.
            age (int): Âge de l'enseignant.
            address (Address): Adresse de l'enseignant.
            phone (int): Numéro de téléphone de l'enseignant.
            mail (str): Adresse e-mail de l'enseignant.
            arrival_date (date): Date d'arrivée de l'enseignant.
        """
        super().__init__(name, surname, age, address, phone, mail, arrival_date)

    def get_details(self) -> str:
        """
        Renvoie les détails de l'enseignant.

        Returns:
            str: Détails de l'enseignant sous forme de chaîne de caractères.
        """
        return f"Nom: {self.get_complete_name()}, E-mail: {self.mail}, Téléphone: {self.phone}"
