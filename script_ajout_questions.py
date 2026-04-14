from app import app, db, Question
from datetime import date

with app.app_context():
    # Suppression des anciennes questions pour éviter les mélanges
    db.session.query(Question).delete()

    # Création de tes 5 questions historiques
    q1 = Question(
        question="En quelle année l’homme a-t-il marché sur la Lune pour la première fois ?", 
        correct_answer="1969"
    )
    q2 = Question(
        question="Qui a été le premier empereur de Rome ?", 
        correct_answer="Auguste"
    )
    q3 = Question(
        question="Quel événement a déclenché la Première Guerre mondiale ?", 
        correct_answer="L'assassinat de l'archiduc François-Ferdinand"
    )
    q4 = Question(
        question="En quelle année est tombé le mur de Berlin ?", 
        correct_answer="1989"
    )
    q5 = Question(
        question="Qui a découvert l’Amérique en 1492 ?", 
        correct_answer="Christophe Colomb"
    )

    # Ajout et validation
    db.session.add_all([q1, q2, q3, q4, q5])
    db.session.commit()

    print("---")
    print("✅ Base de données mise à jour avec tes questions historiques !")
    print("---")

