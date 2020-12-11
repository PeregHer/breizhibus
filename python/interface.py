import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from functools import partial
import re
from connexion import Connexion


color_ids = {'Rouge': '#F44336', 'Bleu': '#03A9F4', 'Vert': '#4CAF50', 'Jaune': '#FFEB3B',
             'Mauve': '#7E57C2', 'Noir': '#000000', 'Rose': '#EC407A', 'BG': '#566573'}


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Breizhibus")
        self.master.geometry('900x600')
        self.master.minsize(900, 600)
        self.master.configure(bg=color_ids['BG'])

        label = tk.Label(self.master, font=(
            'Helvetica', '50'), fg='#ce0033', bg=color_ids['BG'], text="Breizhibus")
        label.pack(fill='x', side='top')

        self.bottom_frame = tk.Frame(self.master, bg=color_ids['BG'])
        self.bottom_frame.pack(side='bottom')

        nom_auteur = tk.Label(self.bottom_frame, font=(
            'Helvetica', '13'), fg='#ce0033', bg=color_ids['BG'], text="Created by Pereg Hergoualc'h")
        nom_auteur.grid(row=0, column=1, sticky='s', padx=125, pady=10)

        self.boutton_menus = tk.Button(self.bottom_frame, height=2, width=13, bg='#ce0033', bd=0, font=(
            'Helvetica', '11'), text="Menu des bus", command=self.menu_bus)
        self.boutton_menus.grid(row=0, column=2, padx=125, pady=10)

        self.frame_menu = tk.Frame(self.master, bg=color_ids['BG'])
        self.frame_menu.pack()

        self.lignes = Connexion.get_lignes()

    def menu_lignes(self):
        for widget in self.frame_menu.winfo_children():
            widget.destroy()

        self.boutton_menus.configure(
            text="Menu des bus", command=self.menu_bus)

        self.frame_lignes = tk.Frame(self.frame_menu, bg=color_ids['BG'])
        self.frame_arrets_bus = tk.Frame(
            self.frame_menu, bg=color_ids['BG'])

        self.frame_lignes.pack(side='top', pady=25)
        self.frame_arrets_bus.pack(side='top', pady=25)

        for i in self.lignes.keys():
            commande = partial(self.afficher_arrets, i)
            ligne = tk.Button(self.frame_lignes, height=2, width=13, bg=color_ids[self.lignes[i]], bd=0, font=(
                'Helvetica', '11'), text=self.lignes[i], command=commande)
            ligne.grid(row=0, column=i, padx=10, ipadx=10)

    def afficher_arrets(self, ligne):
        arrets_liste = Connexion.get_arrets(ligne)
        bus_liste = Connexion.get_bus_ligne(ligne)

        for widget in self.frame_arrets_bus.winfo_children():
            widget.destroy()

        arrets_label = tk.Label(self.frame_arrets_bus, text="Arrets", bg=color_ids['BG'], font=(
            'Helvetica', '20', 'underline'))
        bus_label = tk.Label(self.frame_arrets_bus, text="Bus", bg=color_ids['BG'], font=(
            'Helvetica', '20', 'underline'))
        arrets_label.grid(row=0, column=1, padx=50)
        bus_label.grid(row=0, column=2, padx=50)

        for i, arret in enumerate(arrets_liste, 1):
            arret = tk.Label(
                self.frame_arrets_bus, text=arret, bg=color_ids['BG'], font=('Helvetica', '12'))
            arret.grid(row=i, column=1)

        for i, bus in enumerate(bus_liste, 1):
            bus = tk.Label(self.frame_arrets_bus, text=bus,
                                bg=color_ids['BG'], font=('Helvetica', '12'))
            bus.grid(row=i, column=2)

    def menu_bus(self):
        self.bus = Connexion.get_all_bus()
        self.boutton_menus.configure(
            text="Menu des lignes", command=self.menu_lignes)
        for widget in self.frame_menu.winfo_children():
            widget.destroy()

        frame_bus = tk.Frame(self.frame_menu, bg=color_ids['BG'])
        frame_bus.pack()

        frame_edit = tk.Frame(self.frame_menu, bg=color_ids['BG'])
        frame_edit.pack()

        numero_label = tk.Label(frame_bus, text="Numero", bg=color_ids['BG'], font=(
            'Helvetica', '15', 'underline'))
        immatriculation_label = tk.Label(
            frame_bus, text="Immatriculation", bg=color_ids['BG'], font=('Helvetica', '15', 'underline'))
        nb_places_label = tk.Label(
            frame_bus, text="Nombre places", bg=color_ids['BG'], font=('Helvetica', '15', 'underline'))
        bus_ligne_label = tk.Label(
            frame_bus, text="Ligne", bg=color_ids['BG'], font=('Helvetica', '15', 'underline'))

        numero_label.grid(row=0, column=1, padx=35, ipady=10)
        immatriculation_label.grid(row=0, column=2, padx=35)
        nb_places_label.grid(row=0, column=3, padx=35)
        bus_ligne_label.grid(row=0, column=4, padx=35)

        for i, (key, values) in enumerate(self.bus.items(), 1):
            bus_name = tk.Label(
                frame_bus, text=key, bg=color_ids['BG'], font=('Helvetica', '12'))
            bus_name.grid(row=i, column=1)

            bus_immatriculation = tk.Label(
                frame_bus, text=values['immatriculation'], bg=color_ids['BG'], font=('Helvetica', '12'))
            bus_immatriculation.grid(row=i, column=2)

            bus_nb_places = tk.Label(
                frame_bus, text=values['nb_places'], bg=color_ids['BG'], font=('Helvetica', '12'))
            bus_nb_places.grid(row=i, column=3)

            bus_nom_ligne = tk.Label(
                frame_bus, text=values['nom_ligne'], bg=color_ids['BG'], font=('Helvetica', '12'))
            bus_nom_ligne.grid(row=i, column=4)

        self.bus_numero_menu = ttk.Combobox(
            frame_edit, values=list(self.bus.keys()))
        self.bus_numero_menu.bind('<<ComboboxSelected>>', self.remplir_champs)
        self.bus_numero_menu.grid(
            row=0, column=1, padx=20, pady=30, sticky='s')

        self.bus_immatriculation_entree = tk.Entry(
            frame_edit, bg='white', width=20, justify='center', font=('Helvetica', '10'))
        self.bus_immatriculation_entree.grid(
            row=0, column=2, padx=20, pady=30, sticky='s')

        self.bus_nb_places_entree = tk.Entry(
            frame_edit, bg='white', width=20, justify='center', font=('Helvetica', '10'))
        self.bus_nb_places_entree.grid(
            row=0, column=3, padx=20, pady=30, sticky='s')

        self.bus_ligne_menu = ttk.Combobox(
            frame_edit, values=list(self.lignes.values()))
        self.bus_ligne_menu.grid(row=0, column=4, padx=20, pady=30, sticky='s')

        self.boutton_modifier_bus = tk.Button(frame_edit, height=2, width=13, bg=color_ids['Vert'], bd=0, font=(
            'Helvetica', '11'), text="Ajouter/Modifier", command=self.ajouter_modifier_bus)
        self.boutton_modifier_bus.grid(row=1, column=2)

        self.boutton_supprimer_bus = tk.Button(frame_edit, height=2, width=13, bg=color_ids['Rouge'], bd=0, font=(
            'Helvetica', '11'), text="Supprimer", command=self.supprimer_bus)
        self.boutton_supprimer_bus.grid(row=1, column=3)

    def ajouter_modifier_bus(self):
        if self.check_entrees() == True:
            Connexion.ajouter_modifier_bus(self.bus_numero_menu.get(), self.bus_immatriculation_entree.get(
            ), self.bus_nb_places_entree.get(), self.id_ligne(self.bus_ligne_menu.get()))
            self.menu_bus()

    def supprimer_bus(self):
        Connexion.supprimer_bus(self.bus_numero_menu.get())
        self.menu_bus()

    def remplir_champs(self, numero):
        bus_numero = self.bus_numero_menu.get()
        self.bus_immatriculation_entree.delete(0, 'end')
        self.bus_immatriculation_entree.insert(
            1, self.bus[bus_numero]['immatriculation'])

        self.bus_nb_places_entree.delete(0, 'end')
        self.bus_nb_places_entree.insert(1, self.bus[bus_numero]['nb_places'])

        self.bus_ligne_menu.delete(0, 'end')
        self.bus_ligne_menu.insert(1, self.bus[bus_numero]['nom_ligne'])

    def check_entrees(self):
        busCheck = re.compile("([B]){2}([0-9]){2}")
        immatriculationCheck = re.compile("([A-Z]){2}([0-9]){3}([A-Z]){2}")

        if re.fullmatch(busCheck, str(self.bus_numero_menu.get())) == None:
            msg = "Veuillez saisir un nom de bus au format BBXX"
            tk.messagebox.showinfo("Erreur", msg)
            return False
        if re.fullmatch(immatriculationCheck, str(self.bus_immatriculation_entree.get())) == None:
            msg = "Veuillez saisir une immatriculation valide"
            tk.messagebox.showinfo("Erreur", msg)
            return False
        if int(self.bus_nb_places_entree.get()) < 15:
            msg = "Veuillez saisir un nombre de place supérieur a 15"
            tk.messagebox.showinfo("Erreur", msg)
            return False
        if int(self.bus_nb_places_entree.get()) > 60:
            msg = "Veuillez saisir un nombre de place inferieur a 60"
            tk.messagebox.showinfo("Erreur", msg)
            return False
        return True

    def id_ligne(self, ligne):
        for key, value in self.lignes.items():
            if value == ligne:
                return key
