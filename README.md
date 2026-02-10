#  Classification des Personnages des Simpsons - Deep Learning + Interface Web

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-orange.svg)](https://www.tensorflow.org/)
[![React](https://img.shields.io/badge/React-19.2-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![Accuracy](https://img.shields.io/badge/Accuracy-98.19%25-success.svg)](https://github.com/Adjakim)
[![Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab)](https://colab.research.google.com/)

---

## 📋 Table des Matières

- [Description](#-description-du-projet)
- [Mon Parcours](#-mon-parcours-de-développement)
- [Recommandations](#-recommandations-importantes)
- [Architecture](#-architecture-du-projet)
- [Structure](#-structure-complète-du-projet)
- [Installation](#-installation-et-démarrage)
- [Utilisation](#-utilisation-de-linterface-web)
- [Dataset](#-dataset)
- [Modèles](#-modèles-deep-learning)
- [API Backend](#-api-backend-flask)
- [Résultats](#-résultats-et-performances)
- [Stack Technique](#-stack-technique)
- [Auteur](#-auteur)

---

## 🎯 Description du Projet

Ce projet a débuté comme un **projet académique** de classification d'images, que j'ai décidé de **poursuivre et d'enrichir personnellement** pour en faire un projet  de Deep Learning avec interface web interactive.

### 📖 Mon Parcours de Développement

**Phase 1 - Projet Académique (Base)**
-  Point de départ : Dataset Kaggle des Simpsons
-  Objectif initial : Apprendre les bases du Deep Learning
-  Framework fourni : Structure de base

**Phase 2 - Extension Personnelle (Mon Travail)**
-  J'ai **choisi moi-même** le nombre d'images : **850 par classe** (équilibrage optimal)
-  J'ai **sélectionné** les **13 personnages** les plus iconiques
-  J'ai **testé** 3 environnements : **Marimo** → **Google Colab** → **VS Code**
- J'ai **développé** l'**API Flask** et l'**interface React** entièrement de A à Z
-  J'ai **optimisé** les modèles pour fonctionner sur **CPU** (pas de GPU disponible)
-  J'ai **créé** un système de déploiement complet avec frontend + backend

### 💻 Environnements Utilisés (Mon Expérience)

#### 1️⃣ **Marimo** - Premiers Tests
-  Expérimentation rapide du preprocessing
-  Tests de visualisation


#### 2️⃣ **Google Colab** - Entraînement Principal
-  **Entraînement avec GPU gratuit** (Tesla T4)
-  Notebooks Jupyter interactifs
-  Gain de temps considérable vs CPU
-  Durée :3 jours 

#### 3️⃣ **VS Code** - Développement Final
-  Entraînement final sur **CPU local** (validation)
-  Développement de l'API Flask
-  Création du frontend React
-  Intégration complète
-  Durée : ~2 semaines

---

## 💡 Recommandations IMPORTANTES

### ⚠️ Si Vous N'avez PAS de GPU

** UTILISEZ GOOGLE COLAB !**

**Pourquoi Google Colab ?**
-  **GPU GRATUIT** (Tesla T4 / K80)
-  Entraînement **15-20× plus rapide** qu'un CPU
-  Pas d'installation locale nécessaire
-  Sauvegarde automatique sur Google Drive
-  Parfait pour l'entraînement des modèles

**Mon Expérience :**
-  **CPU (mon PC)** : des heures pour EfficientNet
-  **GPU Colab** : quelques minutes pour le même entraînement
-  **Différence** : **~19× plus rapide !**

**Comment utiliser Google Colab ?**
1. Allez sur [colab.research.google.com](https://colab.research.google.com/)
2. Uploadez vos notebooks `.ipynb`
3. Runtime → Change runtime type → **GPU (T4)**
4. Exécutez vos cellules normalement

**💡 Astuce :** Utilisez Colab pour l'entraînement, puis téléchargez les modèles `.keras` pour les utiliser localement dans l'API Flask !



## 🌟 Ce Que J'ai Appris

### Compétences Techniques
-  Deep Learning avec TensorFlow/Keras
-  Transfer Learning (EfficientNet)
-  API REST avec Flask
-  Frontend React moderne
-  Optimisation pour CPU
-  Gestion de projet Data Science

### Défis Surmontés
-  Entraînement sans GPU (optimisation hyperparamètres)
-  Création d'une interface utilisateur intuitive
-  Intégration backend-frontend
-  Équilibrage du dataset
-  Debugging de modèles Deep Learning

---

##  Architecture du Projet

```
┌───────────────────────────────────┐
│   Frontend React                  │
│   http://localhost:3000           │
│   - Upload d'images               │
│   - Sélection du modèle           │
│   - Affichage des résultats       │
└──────────────┬────────────────────┘
               │
               │ HTTP POST /predict
               │ FormData (image + model)
               ↓
┌───────────────────────────────────┐
│   Backend Flask API               │
│   http://localhost:5000           │
│   - Endpoint /predict             │
│   - Preprocessing                 │
│   - Chargement des modèles        │
└──────────────┬────────────────────┘
               │
               │ model.predict()
               ↓
┌───────────────────────────────────┐
│   Modèles TensorFlow              │
│   - cnn_scratch.keras             │
│   - efficientnet_final.keras      │
│   (Entraînés sur Google Colab)   │
└──────────────┬────────────────────┘
               │
               │ Prédictions + Top 3
               ↓
┌───────────────────────────────────┐
│   Réponse JSON                    │
│   {                               │
│     "prediction": "homer_simpson",│
│     "confidence": 0.9845,         │
│     "top_3": [...]                │
│   }                               │
└───────────────────────────────────┘
```

---

## 📁 Structure Complète du Projet

```
CNN/
├── 📁 data/                              # Données (1.8 GB)
│   ├── 📁 balanced/
│   │   └── 📁 simpsons_balanced/         # 11,050 images (850/classe)
│   │       └── ... (13 classes)
│   │
│   ├── 📁 processed/                     # Train/Val split
│   │   ├── 📁 train/                     # 8,840 images (80%)
│   │   └── 📁 validation/                # 2,210 images (20%)
│   │
│   └── 📁 raw/                           # Dataset original
│
├── 📁 frontend-react/                    # Application React
│   ├── 📁 public/
│   │   └── 🖼️ simpsons_family.jpg
│   │
│   ├── 📁 src/
│   │   ├── ⚛️ App.jsx                    # Composant principal
│   │   └── 📁 components/
│   │       ├── ⚛️ Header.jsx
│   │       ├── ⚛️ ModelSelector.jsx
│   │       ├── ⚛️ ImageUpload.jsx
│   │       ├── ⚛️ Results.jsx
│   │       └── ⚛️ Loading.jsx
│   │
│   └── 📋 package.json
│
├── 📁 models/                            # Modèles entraînés (313 MB)
│   ├── 🧠 cnn_scratch.keras              # CNN (89.86%)
│   └── 🧠 efficientnet_final.keras       # EfficientNet (98.19%)
│
├── 📁 notebooks/                         # Notebooks Jupyter
│   ├── 📓 00_PROJET_SETUP.ipynb          # EDA & Preprocessing
│   └── 📓 01_PROJET_MODELISATION.ipynb   # Entraînement
│
├── 📁 utils/                             # Utilitaires Python
│   ├── 🐍 data_utils.py
│   ├── 🐍 model_utils.py
│   └── 🐍 viz_utils.py
│
├── 🐍 app.py                             # Backend Flask API ⭐
├── ⚙️ config.yaml                        # Configuration
├── 📝 README.md                          # Ce fichier
└── 📄 requirements.txt                   # Dépendances Python

================================================================================
STATISTIQUES
================================================================================
Fichiers Python                    : 5
Fichiers JavaScript/React          : 12
Modèles Keras                      : 2
Notebooks Jupyter                  : 2
Taille totale                      : 1 812,75 MB
Dossiers                           : 92
================================================================================
```

---

##  Installation et Démarrage

### Prérequis

- **Python 3.11** (⚠️ Python 3.14 non supporté par TensorFlow)
- **Node.js 16+** et npm
- **8 GB RAM** minimum
- **2 GB espace disque** libre
- Navigateur moderne

### Option 1 : Avec GPU (Google Colab)

**🎯 RECOMMANDÉ pour l'entraînement !**

1. **Entraînement sur Colab**
```python
# Dans un notebook Colab
!pip install tensorflow pillow numpy pandas matplotlib seaborn
# Exécuter les notebooks d'entraînement
# Télécharger les .keras générés
```

2. **Utilisation locale (API + Frontend)**
```bash
# Installation normale (voir ci-dessous)
```

---

### Option 2 : Sans GPU (CPU uniquement)

**⚠️ L'entraînement sera LONG (+2h30). Privilégiez Colab !**

#### 1️⃣ Cloner le Repository

```bash
git clone https://github.com/Adjakim/cnn-simpsons-classification.git
cd cnn-simpsons-classification
```

#### 2️⃣ Installer les Dépendances Python

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Vérification :**
```bash
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)"
```

**Si erreur TensorFlow :**
```bash
# Vérifier version Python (doit être 3.11 ou 3.12)
python --version

# Si 3.14, installer Python 3.11
# https://www.python.org/downloads/release/python-3110/
```

#### 3️⃣ Installer React

```bash
cd frontend-react
npm install
cd ..
```

#### 4️⃣ Lancer l'Application

**Terminal 1 - Backend :**
```bash
python app.py
```

**Terminal 2 - Frontend :**
```bash
cd frontend-react
npm start
```

**✅ Ouvrez `http://localhost:3000` dans votre navigateur ! 🎉**

---

## 🎮 Utilisation de l'Interface Web

### 1️⃣ Choisir le Modèle

| Modèle | Accuracy | Vitesse | Recommandation |
|--------|----------|---------|----------------|
| **⚡ EfficientNet** | **98.19%** | 3-5s | ⭐ Recommandé |
| **🧠 CNN Scratch** | 89.86% | 2-3s | Comparaison |

### 2️⃣ Charger une Image

**Option A : Upload local**
- Glissez-déposez une image
- Formats : PNG, JPG, JPEG (max 10 MB)

**Option B : URL**
- Collez une URL d'image
- Exemple : `https://upload.wikimedia.org/wikipedia/en/0/02/Homer_Simpson_2006.png`

### 3️⃣ Obtenir la Prédiction

Cliquez **"🔮 Identifier le personnage"**

**Résultat affiché :**
```

Homer Simpson
Confiance : 98.45%

Top 3 Prédictions
🥇 Homer Simpson        98.45%
🥈 Grampa Simpson        1.23%
🥉 Chief Wiggum          0.18%
```

---

##  Dataset

### Source & Modifications

**Dataset original :** [Kaggle - The Simpsons Characters](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset)

**Mes choix personnels :**
-  Sélection de **13 personnages** iconiques (j'ai éliminé les personnages mineurs)
-  Équilibrage à **850 images par classe** (choix optimal après tests)
-  Split **80/20** train/validation

### Statistiques

| Métrique | Valeur |
|----------|--------|
| Classes | 13 personnages |
| Images/classe | 850 (équilibré) |
| Train | 8,840 (80%) |
| Validation | 2,210 (20%) |
| Résolution | 224×224 RGB |
| Taille totale | 1.8 GB |

### Les 13 Personnages (Mon Choix)

1.  Abraham "Grampa" Simpson
2.  Bart Simpson
3.  Charles Montgomery Burns
4.  Chief Wiggum
5. Homer Simpson
6.  Krusty the Clown
7.  Lisa Simpson
8.  Marge Simpson
9. Milhouse Van Houten
10.  Moe Szyslak
11.  Ned Flanders
12. Principal Skinner
13. Sideshow Bob

---

## 🧠 Modèles Deep Learning

### Modèle 1 : CNN From Scratch

**Architecture personnalisée :**
```
Input (224×224×3)
↓
Conv2D (32) → BatchNorm → ReLU → MaxPool
↓
Conv2D (64) → BatchNorm → ReLU → MaxPool
↓
Conv2D (128) → BatchNorm → ReLU → MaxPool
↓
Conv2D (256) → BatchNorm → ReLU → MaxPool
↓
GlobalAvgPool → Dense (256) → Dropout (0.5)
↓
Dense (13) → Softmax
```

**Performances :**
- Accuracy : **89.86%**
- Entraînement : ~45 min (CPU) / ~3 min (Colab GPU)
- Taille : 125 MB

---

### Modèle 2 : Transfer Learning - EfficientNetB0

**Architecture :**
```
EfficientNetB0 (ImageNet pre-trained)
↓
GlobalAvgPool
↓
Dense (256) → Dropout (0.5)
↓
Dense (13) → Softmax
```

**Entraînement 2 phases :**
- **Phase 1** (8 epochs) : Base frozen
- **Phase 2** (12 epochs) : Top 100 layers unfrozen

**Performances :**
- Accuracy : **98.19%** ⭐
- Entraînement : + 2h30 (CPU) / ~8 min (Colab GPU)
- Taille : 188 MB

**Comparaison CPU vs GPU (Mon Expérience) :**

| Environnement | Temps EfficientNet | Temps CNN | Total |
|---------------|-------------------|-----------|-------|
| **Google Colab (GPU)** | 8 min | 3 min | **11 min** ⚡ |
| **Mon PC (CPU)** | 2h30 | 45 min | **3h15** 🐢 |
| **Différence** | **19× plus rapide** | **15× plus rapide** | **18× plus rapide** |

---

##  API Backend Flask

### Endpoints

#### GET `/health`
```bash
curl http://localhost:5000/health
```

**Réponse :**
```json
{
  "status": "OK",
  "models_loaded": {
    "cnn": true,
    "efficientnet": true
  },
  "classes": 13
}
```

---

#### POST `/predict`
```bash
curl -X POST http://localhost:5000/predict \
  -F "image=@homer.jpg" \
  -F "model=efficientnet"
```

**Réponse :**
```json
{
  "success": true,
  "prediction": "homer_simpson",
  "confidence": 0.9845,
  "top_3": [
    {"character": "homer_simpson", "confidence": 0.9845},
    {"character": "abraham_grampa_simpson", "confidence": 0.0123},
    {"character": "chief_wiggum", "confidence": 0.0018}
  ],
  "model_used": "efficientnet"
}
```

---

#### GET `/classes`
```bash
curl http://localhost:5000/classes
```

---

## 📈 Résultats et Performances

### Métriques Finales

| Modèle | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| CNN Scratch | 89.86% | 89.45% | 89.21% | 89.33% |
| **EfficientNet** | **98.19%** | **98.12%** | **98.08%** | **98.10%** |

**Gain EfficientNet vs CNN :** **+8.33%** ⭐

---

## 🛠️ Stack Technique

### Backend
- Python 3.11
- TensorFlow 2.18
- Flask 3.1
- Pillow, NumPy, Pandas

### Frontend
- React 19.2
- Axios
- CSS3 (responsive)

### Environnements
- **Marimo** (tests initiaux)
- **Google Colab** (entraînement GPU)
- **VS Code** (développement final)

---

##  Dépannage

### Erreur TensorFlow

**Erreur :** `No matching distribution found for tensorflow`

**Solution :** Python 3.14 non supporté
```bash
# Installer Python 3.11
python --version  # Doit afficher 3.11.x
```

---

### React Scripts Manquant

**Erreur :** `'react-scripts' is not recognized`

**Solution :**
```bash
cd frontend-react
npm install react-scripts@5.0.1 --save-exact
npm install
```

---

### Entraînement Trop Lent

**Symptôme :** Entraînement prend >1h

**Solution :** **Utilisez Google Colab !**
1. Créez un compte Google
2. Allez sur [colab.research.google.com](https://colab.research.google.com/)
3. Runtime → Change runtime type → **GPU**
4. Uploadez vos notebooks et exécutez !

---

## 📝 Auteur

**Adja Kimy Fatima**  
Passionnée de Data Science & Deep Learning

- 🌐 GitHub : [@Adjakim](https://github.com/Adjakim)
- 📧 Email : adjakimfatima@gmail.com
- 💼 LinkedIn : [Adja Kimy Fatima](https://linkedin.com/in/adjakim)

**Parcours :**
- 🎓 Formation en  Data, IA et DEV (2025-2026)

---


##  Améliorations Futures

### Court Terme
- [ ] Batch predictions
- [ ] Historique des prédictions
- [ ] Support WebP

### Moyen Terme
- [ ] Déploiement cloud (Heroku/Render)
- [ ] Support de 20+ personnages
- [ ] Application mobile

### Long Terme
- [ ] Explicabilité (Grad-CAM)
- [ ] Webcam en temps réel
- [ ] Vision Transformer (ViT)

---

## 💡 Conseils aux Futurs Développeurs

### Si Vous Reproduisez Ce Projet

✅ **FAITES :**
- Utilisez **Google Colab** pour l'entraînement (GPU gratuit)
- Testez d'abord avec **un petit dataset** (100 images)
- Sauvegardez **régulièrement** vos modèles (`.keras`)
- Utilisez **Git** dès le début

❌ **ÉVITEZ :**
- Entraîner sur CPU si vous avez accès à Colab
- Utiliser tout le dataset d'un coup (commencez petit)
- Négliger la documentation
- Oublier de sauvegarder vos notebooks

### Mon Plus Grand Apprentissage

**"L'accès au GPU change TOUT !"**

Avant Colab :+3h15 d'entraînement 🐢  
Avec Colab GPU : 11 minutes ⚡  

**Différence : 18× plus rapide !**

---

<div align="center">

**🎬 Simpsons Character Classifier**

Fait avec ❤️ par [Adja Kimy Fatima](https://github.com/Adjakim)

**Dernière mise à jour** : Février 2026 | **Version** : 2.0

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-orange.svg)](https://www.tensorflow.org/)
[![React](https://img.shields.io/badge/React-19.2-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab)](https://colab.research.google.com/)



⭐ **Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !**

