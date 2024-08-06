from datetime import date
from person import Person
from address import Address
from academic_record import AcademicRecord


class Student(Person):
    """
    Classe représentant un étudiant, héritant de la classe Person.

    Attributs:
        id (int): Identifiant de l'étudiant.
        parent (Parent): Parent de l'étudiant.
        academic_record (AcademicRecord): Dossier académique de l'étudiant.
    """

    def __init__(self, name: str, surname: str, age: int, address: Address, phone: int, mail: str, arrival_date: date,
                 id: int, parent: 'Parent', academic_record: AcademicRecord):
        """
        Initialise un nouvel étudiant.

        Args:
            name (str): Prénom de l'étudiant.
            surname (str): Nom de famille de l'étudiant.
            age (int): Âge de l'étudiant.
            address (Address): Adresse de l'étudiant.
            phone (int): Numéro de téléphone de l'étudiant.
            mail (str): Adresse e-mail de l'étudiant.
            arrival_date (date): Date d'arrivée de l'étudiant.
            id (int): Identifiant de l'étudiant.
            parent (Parent): Parent de l'étudiant.
            academic_record (AcademicRecord): Dossier académique de l'étudiant.
        """
        super().__init__(name, surname, age, address, phone, mail, arrival_date)
        self.id = id
        self.parent = parent
        self.academic_record = academic_record

    def get_details(self) -> str:
        """
        Renvoie les détails de l'étudiant.

        Returns:
            str: Détails de l'étudiant sous forme de chaîne de caractères.
        """
        return f"ID: {self.id}, Nom: {self.get_complete_name()}, Dossier académique: {self.academic_record.get_details()}"
