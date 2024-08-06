class Address:
    """
    Classe représentant une adresse.

    Attributs:
        street (str): Rue de l'adresse.
        city (str): Ville de l'adresse.
        postal_code (str): Code postal de l'adresse.
    """

    def __init__(self, street: str, city: str, postal_code: str):
        """
        Initialise une nouvelle adresse.

        Args:
            street (str): Rue de l'adresse.
            city (str): Ville de l'adresse.
            postal_code (str): Code postal de l'adresse.
        """
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def to_string(self) -> str:
        """
        Renvoie une représentation en chaîne de caractères de l'adresse.

        Returns:
            str: Adresse complète sous forme de chaîne de caractères.
        """
        return f"{self.street}, {self.city}, {self.postal_code}"
