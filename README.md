# Gestion de Bibliothèque (CLI Python)

Application console de gestion de bibliothèque développée en **Python** avec une base de données **SQLite**, structurée selon une architecture modulaire et versionnée avec **Git/GitHub**.

---

## 🚀 Présentation du projet
Ce projet permet de gérer le catalogue d'une bibliothèque directement depuis un terminal (CLI). Il offre un suivi en temps réel de la disponibilité des livres (emprunts et retours) et garantit une séparation claire entre l'interface utilisateur, la logique métier et la gestion de la base de données.

---

## ✨ Fonctionnalités disponibles
1. **Ajouter un livre** : Enregistrement d'un nouveau livre avec son titre, son auteur et son année de publication.
2. **Afficher les livres** : Liste complète de tous les livres présents dans la base avec leur statut (Disponible ou Emprunté).
3. **Rechercher un livre** : Recherche flexible par titre ou par auteur (insensible à la casse partielle).
4. **Emprunter un livre** : Modification du statut d'un livre en "Emprunté" (si disponible).
5. **Retourner un livre** : Remise en circulation d'un livre emprunté.
6. **Supprimer un livre** : Suppression définitive d'un livre de la base de données (sécurisée par une confirmation obligatoire).

---

## ⚙️ Instructions d'installation
1. Assurez-vous d'avoir **Python** installé sur votre machine.
2. Clonez le dépôt ou téléchargez les fichiers du projet dans un dossier local :
   ```bash
   git clone [https://github.com/younesfrd/projet-bibliotheque.git](https://github.com/younesfrd/projet-bibliotheque.git)
   cd projet-bibliotheque