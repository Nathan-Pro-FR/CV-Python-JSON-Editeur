# 🚀 GUIDE TECHNIQUE — CV INTERACTIF PREMIUM (v8)

[![Pylint](https://github.com/Nathan-Pro-FR/CV-Python-JSON-Editeur/actions/workflows/pylint.yml/badge.svg)](https://github.com/Nathan-Pro-FR/CV-Python-JSON-Editeur/actions/workflows/pylint.yml)

Ce guide complet t'explique comment mettre à jour le contenu textuel de ton CV ou modifier son apparence graphique à l'aide des deux fichiers de configuration externes.

Language utilisées : 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

---

## 📌 Sommaire

```txt
📂 cv_data.json .......... Éditeur de contenu textuel
└── ⚠️ 3 Règles d'or du JSON
🎨 theme_config.json ..... Personnalisation graphique
├── 💡 Couleurs du texte (Tableau interactif)
├── 🔮 Ambiance Lava Lamp
└── 🎯 Détection des icônes

```

## 📂 1. L'Éditeur de Contenu (cv_data.json)
Pour modifier les textes de ton CV, **tu n'as plus besoin de toucher au code Python**. Ouvre simplement le fichier cv_data.json avec le Bloc-notes ou VS Code.
> [!IMPORTANT]
> ### ⚠️ LES 3 RÈGLES D'OR DU JSON
>  1. **Les guillemets** : Le texte doit toujours être entouré de guillemets doubles : "mon texte".
>  2. **Les sauts de ligne** : Pour faire un retour à la ligne dans l'application, utilise le code \n **à l'intérieur** de tes guillemets.
>  3. **La virgule finale** : La toute dernière clé du fichier ne doit **pas** avoir de virgule , à la fin, sinon le programme plante.
> 
<details>
<summary>💡 <b>Clique ici pour voir un exemple de structure valide</b></summary>
  
```json
{
  "Profil": "👋 TITRE PRINCIPAL\n\nIci mon paragraphe de texte.\n• Une puce ici.",
  "Contact": "📞 COORDONNÉES\n\nMon téléphone..."
}
```

</details>

## 🎨 2. Personnalisation Visuelle (theme_config.json)
Pour modifier l'univers graphique (couleurs du texte, des puces, des bulles) ou ajouter un nouvel émoji à détecter, tout se passe dans le fichier theme_config.json.

### 🎛️ Options de configuration disponibles

#### 💡 Couleurs du texte (couleurs_texte)

| Élément | Rôle | Aperçu / Teinte |
|---|---|---|
| "texte_standard" | Couleur des paragraphes de texte par défaut | #cbd5e1 (Gris) |
| "titre_principal" | Couleur de la première ligne et de l'onglet actif | #38bdf8 (Bleu) |
| "sous_titres_maj" | Couleur des lignes écrites entièrement en MAJUSCULES | #ffffff (Blanc) |
| "puces_emojis" | Couleur des icônes et symboles détectés | #34d399 (Vert) |
| "curseur_clignotant" | Couleur du carré d'écriture dynamique █ | #38bdf8 (Bleu) |

#### 🔮 Ambiance d'arrière-plan (couleurs_lava_lamp)
Modifie ou ajoute des codes hexadécimaux dans cette liste pour changer instantanément la teinte des bulles de cire animées en fond d'écran.

🎨 **Palette actuelle** : #1e3a8a | #0d9488 | #4c1d95 | #0369a1

#### 🎯 Détection des icônes (puces_detectees)
Ajoute simplement ton nouvel émoji entre guillemets, séparé par une virgule.

> [!TIP]
> L'application détecte l'icône automatiquement s'il se trouve **au début d'une ligne** et lui applique la couleur définie pour "puces_emojis".
>

<details>
<summary>🌐 <b>Clique ici pour afficher le fichier theme_config.json complet</b></summary>

  ```json
{
  "couleurs_texte": {
    "texte_standard": "#cbd5e1",
    "titre_principal": "#38bdf8",
    "sous_titres_maj": "#ffffff",
    "puces_emojis": "#34d399",
    "curseur_clignotant": "#38bdf8"
  },
  "couleurs_lava_lamp": [
    "#1e3a8a",
    "#0d9488",
    "#4c1d95",
    "#0369a1"
  ],
  "puces_detectees": [
    "•", "▶", "-", "👋", "⚡", "💼", "🚀"
  ]
}

```
</details>
# CV-Python-JSON-Editeur
