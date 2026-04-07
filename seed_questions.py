from app import app, db, Question  # Tout est dans app.py
from datetime import date

with app.app_context():
    # Créer les nouvelles questions
    q1 = Question(question="Quel est le plus grand océan du monde ?", correct_answer="Pacifique")
    q2 = Question(question="En quelle année a été créé le langage Python ?", correct_answer="1991")
    q3 = Question(question="Quel organe humain consomme le plus d'énergie ?", correct_answer="Le cerveau")
    q4 = Question(question="Quel est le symbole chimique de l'or ?", correct_answer="Au")
    q5 = Question(question="Qui a écrit 'Les Misérables' ?", correct_answer="Victor Hugo")

    # Ajouter à la base
    db.session.add_all([q1, q2, q3, q4, q5])
    db.session.commit()

    print("✅ Nouvelles questions ajoutées avec succès !")

