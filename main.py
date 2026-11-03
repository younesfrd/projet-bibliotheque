from database import initialiser_base
from livre_service import ajouter_livre ,afficher_livre,recher_livre,emprunter_livre,retourner_livre,supprimer_livre
def menu():
    initialiser_base()
    while True :
        print("""====================================
  	GESTION DE BIBLIOTHÈQUE
====================================
1 - Ajouter un livre
2 - Afficher les livres
3 - Rechercher un livre
4 - Emprunter un livre
5 - Retourner un livre
6 - Supprimer un livre
0 - Quitter
""")
        choix_de_saisie=input("votre choix : ")
        if choix_de_saisie == "1" :
            titre=input("donnez le titre du livre : ")
            auteur=input("donnez l'auteur du livre : ")
            try :
               annee=int(input("donnez l'année de sortie du livre : "))
               ajouter_livre(titre,auteur,annee) 
            except ValueError :
              print("entrez un nombre : ")       
        elif  choix_de_saisie == "2" :
            livres = afficher_livre()
            if not livres :
                print("bibliotheque vide")
            else :
                print(f"{'ID':<4} | {'TITRE':<25} | {'AUTEUR':<20} | {'ANNEE':<6}")
                print("-" * 65)
                for li in livres :
                  print(f"{li[0]:<4} | {li[1]:<25} | {li[2]:<20} | {li[3]:<6}")
                print("-" * 65)
        elif choix_de_saisie == "3":
           mot=input("enter le mot de cherche : ").strip()
           resultat=recher_livre(mot)
           print(f"{'ID':<4} | {'TITRE':<25} | {'AUTEUR':<20} | {'ANNEE':<6}")
           print("-" * 65)
           for re in resultat:
              print(f"{re[0]:<4} | {re[1]:<25} | {re[2]:<20} | {re[3]:<6}")
           print("-" * 65)
        elif choix_de_saisie =="4" :
                try:
                    id_livre = int(input("Entrez l'ID du livre à emprunter : "))
                    statut = emprunter_livre(id_livre)
                    if statut == "succes":
                        print("Livre emprunté avec succès ! Bon lecture.")
                    elif statut == "deja_emprunte":
                        print("Erreur : Ce livre est déjà emprunté par quelqu'un d'autre.")
                    elif statut == "inexistant":
                        print("Erreur : Aucun livre ne correspond à cet ID.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide pour l'ID.")
                print("-" * 35)
        elif choix_de_saisie == "5":
                try:
                    id_livre = int(input("Entrez l'ID du livre à retourner : "))
                    statut = retourner_livre(id_livre)
                    if statut == "succes":
                        print("Livre retourné avec succès ! Il est de nouveau disponible.")
                    elif statut == "deja_disponible":
                        print("Erreur : Ce livre n'était pas emprunté (il est déjà dans la bibliothèque).")
                    elif statut == "inexistant":
                        print("Erreur : Aucun livre ne correspond à cet ID.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide pour l'ID.")
                print("-" * 35)
        elif choix_de_saisie=="6":
            try:
                    id_livre = int(input("Entrez l'ID du livre à supprimer : "))
                    confirmation = input(f"Êtes-vous sûr de vouloir supprimer le livre n°{id_livre} ? (o/n) : ").strip().lower()
                    if confirmation in ['o', 'oui']:
                        statut = supprimer_livre(id_livre)  
                        if statut == "succes":
                            print("Livre supprimé avec succès de la base de données.")
                        elif statut == "inexistant":
                            print("Erreur : Aucun livre ne correspond à cet ID.")
                    else:
                        print("Suppression annulée.")          
            except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide pour l'ID.")
                    print("-" * 35)
        elif choix_de_saisie=="0":
            print("au revoir !!")
        else :
            print("ecrivez un nombre qui corresponds a la liste")
                   
menu()        

