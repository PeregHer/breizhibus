import mysql.connector as mysql


class Connexion:
    @classmethod
    def ouvrir_connexion(cls):
        cls.link = mysql.connect(user='root', password='root', host='localhost', port=8081, database='breizhibus')
        cls.cursor = cls.link.cursor()

    @classmethod
    def fermer_connexion(cls):
        cls.cursor.close()
        cls.link.close()
    
    @classmethod
    def get_lignes(cls):
        cls.ouvrir_connexion()
        lignes = {}
        cls.cursor.execute("SELECT id_ligne, nom FROM lignes")
        for _id, nom in cls.cursor.fetchall():
            lignes[_id] = nom
        cls.fermer_connexion()
        return lignes

    @classmethod
    def get_arrets(cls, ligne):
        cls.ouvrir_connexion()
        cls.cursor.execute(f"SELECT nom FROM arrets JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret WHERE id_ligne = {ligne}")
        arrets =  cls.cursor.fetchall()
        cls.fermer_connexion()
        return arrets

    @classmethod
    def get_bus_ligne(cls, ligne):
        cls.ouvrir_connexion()
        cls.cursor.execute(f"SELECT numero FROM bus WHERE id_ligne = {ligne}")
        bus = cls.cursor.fetchall()
        cls.fermer_connexion()
        return bus

    @classmethod
    def get_all_bus(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute(f"SELECT numero, immatriculation, nombre_places, lignes.nom FROM bus JOIN lignes ON lignes.id_ligne = bus.id_ligne ORDER BY bus.numero")
        bus = {}
        for item in cls.cursor.fetchall():
            bus[item[0]] = {'immatriculation': item[1], 'nb_places': item[2], 'nom_ligne': item[3]}
        cls.fermer_connexion()
        return bus

    @classmethod
    def get_bus_id(cls, numero):
        try:
            cls.cursor.execute(f"SELECT id_bus, immatriculation, nombre_places, id_ligne FROM bus WHERE numero = '{numero}'")
            _id = cls.cursor.fetchall()[0][0]
            return _id
        except:
            return None

    @classmethod
    def ajouter_modifier_bus(cls, numero, immatriculation, nb_places, ligne):
        cls.ouvrir_connexion()
        values = (cls.get_bus_id(numero), numero, immatriculation, nb_places, ligne, immatriculation, nb_places, ligne)
        SQL = """INSERT INTO bus (id_bus, numero, immatriculation, nombre_places, id_ligne)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE immatriculation=%s,  nombre_places=%s, id_ligne=%s"""
        cls.cursor.execute(SQL, values)
        cls.link.commit()
        cls.fermer_connexion()
        print("Bus modifié/ajouté")

    @classmethod
    def supprimer_bus(cls, numero):
        cls.ouvrir_connexion()
        cls.cursor.execute(f"DELETE FROM bus WHERE bus.numero = '{numero}'")
        cls.link.commit()
        print("Bus supprimé")
        cls.fermer_connexion()