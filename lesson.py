from datetime import date


class Lesson:
    """
    Classe représentant une leçon.

    Attributs:
        denomination (str): Dénomination de la leçon.
        start_date (date): Date de début de la leçon.
        end_date (date): Date de fin de la leçon.
    """

    def __init__(self, denomination: str, start_date: date, end_date: date):
        """
        Initialise une nouvelle leçon.

        Args:
            denomination (str): Dénomination de la leçon.
            start_date (date): Date de début de la leçon.
            end_date (date): Date de fin de la leçon.
        """
        self.denomination = denomination
        self.start_date = start_date
        self.end_date = end_date

    def get_details(self) -> str:
        """
        Renvoie les détails de la leçon.

        Returns:
            str: Détails de la leçon sous forme de chaîne de caractères.
        """
        return f"Leçon: {self.denomination}, Du: {self.start_date}, Au: {self.end_date}"
