import tkinter as tk
import random
import json
import os
import math

class CVNathanLavaPremium:
    def __init__(self, root):
        self.root = root
        self.root.title("CV Interactif - Édition Suprême - Nathan Lacroix")
        self.root.geometry("950x620")
        
        # Chargement des fichiers JSON externes (Données + Design + Puces)
        self.cv_data = self.charger_donnees_externes("cv_data.json", {"Profil": "⚠️ Fichier 'cv_data.json' introuvable !"})
        self.theme = self.charger_donnees_externes("theme_config.json", {
            "couleurs_texte": {
                "texte_standard": "#cbd5e1", "titre_principal": "#38bdf8", 
                "sous_titres_maj": "#ffffff", "puces_emojis": "#34d399", "curseur_clignotant": "#38bdf8"
            },
            "couleurs_lava_lamp": ["#1e3a8a", "#0d9488", "#4c1d95", "#0369a1"],
            "puces_detectees": ["•", "▶", "-", "👋", "⚡", "💼", "🎓", "📜", "🗣", "📞", "💻", "🎨", "🧠", "📍", "✉", "📱"]
        })

        self.root.configure(bg="#0f172a")
        self.animation_application_id = None
        self.bouton_actif = None
        
        self.lignes_a_ecrire = []
        self.index_ligne = 0
        self.index_caractere = 0
        self.compteur_clignotement = 0
        
        self.text_objects = []
        self.text_styles = [] 
        self.curseur_id = None
        self.bulles = []
        
        self.creer_interface()
        self.init_lava_lamp()
        self.animer_application()
        self.canvas.bind("<Configure>", self.redimensionner_texte_auto)

    def charger_donnees_externes(self, nom_fichier, version_secours):
        if os.path.exists(nom_fichier):
            with open(nom_fichier, "r", encoding="utf-8") as f:
                return json.load(f)
        return version_secours

    def creer_interface(self):
        self.sidebar = tk.Frame(self.root, bg="#1e293b", width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        couleur_accent = self.theme["couleurs_texte"]["titre_principal"]
        self.indicator = tk.Frame(self.sidebar, bg=couleur_accent, width=4)
        self.indicator.place(x=0, y=-50, height=45)

        tk.Label(self.sidebar, text="NATHAN LACROIX", font=("Segoe UI", 12, "bold"), bg="#1e293b", fg=couleur_accent, pady=15).pack()
        tk.Label(self.sidebar, text="Stage d'observation", font=("Segoe UI", 9, "italic"), bg="#1e293b", fg="#94a3b8").pack(pady=(0, 15))

        self.boutons = {}
        for cle in self.cv_data.keys():
            btn = tk.Button(self.sidebar, text=f"  {cle}", font=("Segoe UI", 11), bg="#1e293b", fg="#cbd5e1",
                            activebackground="#0f172a", activeforeground=couleur_accent, bd=0, cursor="hand2",
                            anchor="w", padx=15, pady=12, command=lambda c=cle: self.clic_onglet(c))
            btn.pack(fill="x")
            btn.bind("<Enter>", lambda e, b=btn: self.survol_btn(b))
            btn.bind("<Leave>", lambda e, b=btn: self.quitter_btn(b))
            self.boutons[cle] = btn

        self.main_container = tk.Frame(self.root, bg="#0f172a")
        self.main_container.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_container, bg="#0f172a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.clic_onglet(list(self.cv_data.keys())[0])

    def init_lava_lamp(self):
        couleurs = self.theme["couleurs_lava_lamp"]
        for i in range(4):
            rayon = random.randint(75, 105)
            x = random.randint(150, 550)
            y = random.randint(100, 500)
            couleur_bulle = couleurs[i % len(couleurs)]
            
            id_bulle = self.canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=couleur_bulle, outline="")
            self.bulles.append({
                'id': id_bulle, 'x': x, 'y': y, 'base_r': rayon, 'r': rayon,
                'vitesse_y': random.uniform(-0.4, -0.8), 'temperature': random.uniform(0.3, 0.9),
                'angle': random.uniform(0, math.pi * 2), 'vitesse_osc': random.uniform(0.01, 0.02)
            })

    def animer_lava_lamp(self):
        hauteur_canvas = self.canvas.winfo_height() or 600
        for b in self.bulles:
            if b['y'] < hauteur_canvas * 0.25: b['temperature'] -= 0.004
            elif b['y'] > hauteur_canvas * 0.75: b['temperature'] += 0.005
            b['temperature'] = max(0.0, min(1.0, b['temperature']))
            b['vitesse_y'] = -1.6 * (b['temperature'] - 0.45)
            b['y'] += b['vitesse_y']
            b['angle'] += b['vitesse_osc']
            b['r'] = b['base_r']

        for i in range(len(self.bulles)):
            for j in range(i + 1, len(self.bulles)):
                b1, b2 = self.bulles[i], self.bulles[j]
                dist = math.hypot(b1['x'] - b2['x'], b1['y'] - b2['y'])
                somme_rayons = b1['base_r'] + b2['base_r']
                if dist < somme_rayons * 1.3:
                    effet = (1.0 - (dist / (somme_rayons * 1.3))) * 22
                    b1['r'] += effet
                    b2['r'] += effet

        for b in self.bulles:
            x_reel = b['x'] + math.sin(b['angle']) * 25
            self.canvas.coords(b['id'], x_reel - b['r'], b['y'] - b['r'], x_reel + b['r'], b['y'] + b['r'])

    def gerer_machine_a_ecrire(self):
        if self.index_ligne < len(self.lignes_a_ecrire):
            ligne_complete = self.lignes_a_ecrire[self.index_ligne]
            if not ligne_complete.strip():
                if len(self.text_objects) <= self.index_ligne:
                    self.text_objects.append(self.canvas.create_text(0, 0, text=""))
                    self.text_styles.append((self.theme["couleurs_texte"]["texte_standard"], ("Consolas", 11)))
                self.index_ligne += 1
                self.index_caractere = 0
                return

            largeur_max = max(200, self.canvas.winfo_width() - 80)
            pos_y = 40
            for k in range(self.index_ligne):
                bbox = self.canvas.bbox(self.text_objects[k])
                pos_y += (bbox[3] - bbox[1]) + 8 if bbox else 20

            color = self.theme["couleurs_texte"]["texte_standard"]
            font_style = ("Consolas", 11)
            if self.index_ligne == 0:
                color = self.theme["couleurs_texte"]["titre_principal"]
                font_style = ("Consolas", 13, "bold")
            elif ligne_complete.strip().isupper() and len(ligne_complete.strip()) > 4:
                color = self.theme["couleurs_texte"]["sous_titres_maj"]
                font_style = ("Consolas", 11, "bold")

            texte_partiel = ligne_complete[:self.index_caractere]
            if len(self.text_objects) > self.index_ligne:
                self.canvas.delete(self.text_objects[self.index_ligne])
                self.text_objects.pop(self.index_ligne)

            obj_id = self.canvas.create_text(40, pos_y, anchor="nw", text=texte_partiel, fill=color, font=font_style, width=largeur_max)
            self.text_objects.insert(self.index_ligne, obj_id)
            if len(self.text_styles) <= self.index_ligne: self.text_styles.append((color, font_style))

            # Lecture directe des puces depuis le fichier de configuration externe !
            if texte_partiel and texte_partiel[0] in self.theme["puces_detectees"]:
                c_puce = self.theme["couleurs_texte"]["puces_emojis"]
                puce_id = self.canvas.create_text(40, pos_y, anchor="nw", text=texte_partiel[0], fill=c_puce, font=("Consolas", 11, "bold"))
                self.text_objects.append(puce_id)

            if self.curseur_id: self.canvas.delete(self.curseur_id)
            bbox_actuelle = self.canvas.bbox(obj_id)
            if bbox_actuelle:
                c_curseur = self.theme["couleurs_texte"]["curseur_clignotant"]
                self.curseur_id = self.canvas.create_text(bbox_actuelle[2] + 2, bbox_actuelle[3] - 18, anchor="nw", text="█", fill=c_curseur, font=font_style)

            if self.index_caractere < len(ligne_complete): self.index_caractere += 1
            else: self.index_ligne += 1; self.index_caractere = 0
        else:
            if self.curseur_id:
                c_curseur = self.theme["couleurs_texte"]["curseur_clignotant"]
                self.canvas.itemconfig(self.curseur_id, fill=c_curseur if (self.compteur_clignotement // 15) % 2 == 0 else "")

    def redimensionner_texte_auto(self, event):
        largeur_max = max(200, event.width - 80)
        pos_y = 40
        for idx, obj in enumerate(self.text_objects):
            if idx < len(self.text_styles):
                self.canvas.coords(obj, 40, pos_y)
                self.canvas.itemconfig(obj, width=largeur_max)
                bbox = self.canvas.bbox(obj)
                pos_y += (bbox[3] - bbox[1]) + 8 if bbox else 20

    def animer_application(self):
        self.animer_lava_lamp()
        self.gerer_machine_a_ecrire()
        self.compteur_clignotement += 1
        for obj in self.text_objects: self.canvas.tag_raise(obj)
        if self.curseur_id: self.canvas.tag_raise(self.curseur_id)
        self.animation_application_id = self.root.after(20, self.animer_application)

    def survol_btn(self, btn):
        if btn != self.bouton_actif: btn.config(bg="#334155", fg="#ffffff")

    def quitter_btn(self, btn):
        if btn != self.bouton_actif: btn.config(bg="#1e293b", fg="#cbd5e1")

    def clic_onglet(self, cle):
        target_y = self.boutons[cle].winfo_y() if cle in self.boutons else -50
        self.animer_indicateur(target_y)
        if self.bouton_actif and cle in self.boutons: self.bouton_actif.config(bg="#1e293b", fg="#cbd5e1")
        if cle in self.boutons:
            self.bouton_actif = self.boutons[cle]
            self.bouton_actif.config(bg="#0f172a", fg=self.theme["couleurs_texte"]["titre_principal"])

        for obj in self.text_objects: self.canvas.delete(obj)
        if self.curseur_id: self.canvas.delete(self.curseur_id)
        self.text_objects = []; self.text_styles = []; self.curseur_id = None
        self.lignes_a_ecrire = self.cv_data[cle].split('\n')
        self.index_ligne = 0; self.index_caractere = 0

    def animer_indicateur(self, target_y):
        if target_y == -50: return
        curr_y = self.indicator.winfo_y()
        step = (target_y - curr_y) / 4
        self.indicator.place(y=curr_y + step) if abs(step) > 0.1 else self.indicator.place(y=target_y)

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = CVNathanLavaPremium(fenetre)
    fenetre.mainloop()
