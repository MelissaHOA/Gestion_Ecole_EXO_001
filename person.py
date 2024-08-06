from datetime import date
from address import Address


class Person:
    """
    Classe représentant une personne.

    Attributs:
        name (str): Prénom de la personne.
        surname (str): Nom de famille de la personne.
        age (int): Âge de la personne.
        address (Address): Adresse de la personne.
        phone (int): Numéro de téléphone de la personne.
        mail (str): Adresse e-mail de la personne.
        arrival_date (date): Date d'arrivée de la personne.
    """

    def __init__(self, name: str, surname: str, age: int, address: Address, phone: int, mail: str, arrival_date: date):
        """
        Initialise une nouvelle personne.

        Args:
            name (str): Prénom de la personne.
            surname (str): Nom de famille de la personne.
            age (int): Âge de la personne.
            address (Address): Adresse de la personne.
            phone (int): Numéro de téléphone de la personne.
            mail (str): Adresse e-mail de la personne.
            arrival_date (date): Date d'arrivée de la personne.
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone = phone
        self.mail = mail
        self.arrival_date = arrival_date

    def get_complete_name(self) -> str:
        """
        Renvoie le nom complet de la personne.

        Returns:
            str: Nom complet sous forme de chaîne de caractères.
        """
        return f"{self.name} {self.surname}"

    def modify_address(self, new_address: Address):
        """
        Modifie l'adresse de la personne.

        Args:
            new_address (Address): Nouvelle adresse.
        """
        self.address = new_address
