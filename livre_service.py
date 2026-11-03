from database import get_connection
def ajouter_livre(titre,auteur,annee):
    connexion = get_connection()
    curseur = connexion.cursor()
    curseur.execute("""
        INSERT INTO livres (titre, auteur, annee) 
        VALUES (?, ?, ?)
    """, (titre, auteur, annee))
    connexion.commit()
    connexion.close()
    print("livre ajouté")
def afficher_livre():
    conn = get_connection()
    curseur = conn.cursor()
    curseur.execute("SELECT * FROM livres")
    livres = curseur.fetchall()
    conn.close()
    return livres
def recher_livre(mot):
    conn = get_connection()
    curseur = conn.cursor()
    recherche_sql = f"%{mot}%"
    curseur.execute("""
        SELECT * FROM livres 
        WHERE titre LIKE ? OR auteur LIKE ?
    """, (recherche_sql,recherche_sql,))
    resultat = curseur.fetchall()
    conn.close()
    return resultat
def emprunter_livre(id_livre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT titre, disponible FROM livres WHERE id = ?", (id_livre,))
    livre = cursor.fetchone()
    if not livre:
        conn.close()
        return "inexistant"
    titre, disponible = livre
    if disponible == 0:
        conn.close()
        return "deja_emprunte"
    else :
        cursor.execute("""
        UPDATE livres 
        SET disponible = 0 
        WHERE id = ?
    """, (id_livre,))
    conn.commit()
    conn.close()
    return "succes"
def retourner_livre(id_livre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT titre, disponible FROM livres WHERE id = ?", (id_livre,))
    livre = cursor.fetchone()
    if not livre:
        conn.close()
        return "inexistant"
    titre, disponible = livre
    if disponible == 1:
        conn.close()
        return "deja_disponible"
    cursor.execute("""
        UPDATE livres 
        SET disponible = 1 
        WHERE id = ?
    """, (id_livre,))
    conn.commit()
    conn.close()
    return "succes"
def supprimer_livre(id_livre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM livres WHERE id = ?", (id_livre,))
    livre = cursor.fetchone() 
    if not livre:
        conn.close()
        return "inexistant"
    cursor.execute("DELETE FROM livres WHERE id = ?", (id_livre,)) 
    conn.commit()
    conn.close()  
    return "succes"

