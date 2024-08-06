from student import Student


class Parent:
    """
    Classe représentant un parent.

    Attributs:
        student (Student): Étudiant associé au parent.
    """

    def __init__(self, student: 'Student'):
        """
        Initialise un nouveau parent.

        Args:
            student (Student): Étudiant associé au parent.
        """
        self.student = student

    def get_details(self) -> str:
        """
        Renvoie les détails du parent.

        Returns:
            str: Détails du parent sous forme de chaîne de caractères.
        """
        return f"Parent de l'étudiant ID: {self.student.id}"
