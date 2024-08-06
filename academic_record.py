class AcademicRecord:
    """
    Classe représentant un dossier académique.

    Attributs:
        score (int): Score académique.
        comment (str): Commentaire sur le dossier académique.
        level_class (str): Niveau de classe.
    """

    def __init__(self, score: int, comment: str, level_class: str):
        """
        Initialise un nouveau dossier académique.

        Args:
            score (int): Score académique.
            comment (str): Commentaire sur le dossier académique.
            level_class (str): Niveau de classe.
        """
        self.score = score
        self.comment = comment
        self.level_class = level_class

    def get_details(self) -> str:
        """
        Renvoie les détails du dossier académique.

        Returns:
            str: Détails du dossier académique sous forme de chaîne de caractères.
        """
        return f"Score: {self.score}, Commentaire: {self.comment}, Niveau de classe: {self.level_class}"
