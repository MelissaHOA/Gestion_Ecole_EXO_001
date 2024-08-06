from datetime import date


class Absence:
    """
    Classe représentant une absence.

    Attributs:
        date (date): Date de l'absence.
        reason (str): Raison de l'absence.
    """

    def __init__(self, date: date, reason: str):
        """
        Initialise une nouvelle absence.

        Args:
            date (date): Date de l'absence.
            reason (str): Raison de l'absence.
        """
        self.date = date
        self.reason = reason

    def add_absence(self):
        """
        Ajoute une absence.
        """
        # Code pour ajouter une absence
        pass

    def modify_absence(self):
        """
        Modifie une absence.
        """
        # Code pour modifier une absence
        pass

    def delete_absence(self):
        """
        Supprime une absence.
        """
        # Code pour supprimer une absence
        pass

    def consult_absence(self):
        """
        Consulte les détails de l'absence.
        """
        # Code pour consulter les détails de l'absence
        pass
