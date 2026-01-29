# Architecture bloc 2 RNCP38919
---------------Projet ETL & Machine Learning----------------------
## 1. Contexte & Objectif


Ce projet a pour objectif de concevoir et implémenter un pipeline data complet à partir de données JSON, intégrant :

* un traitement ETL robuste,
* une base de données relationnelle,
* un modèle de machine learning,
* un traitement batch et streaming,
* un environnement dockerisé prêt pour la production.

Le projet respecte les bonnes pratiques de structuration, de reproductibilité et de séparation des responsabilités.

---

## 2. Architecture globale

### Schéma d’architecture (logique & fonctionnel)

```text
                ┌──────────────────────┐
                │   Fichier JSON brut   │
                │  (data/raw/raw.json)   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Notebook Jupyter    │
                │ Exploration / Analyse │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │      ETL Python       │
                │ extract / transform   │
                │ scripts/etl.py        │
                └──────────┬───────────┘
                           │
          ┌────────────────┴───────────────┐
          ▼                                ▼
┌───────────────────┐          ┌────────────────────┐
│ JSON nettoyé      │          │ Base MySQL (Docker) │
│ data/processed    │◄────────►│ SQLAlchemy ORM     │
└─────────┬─────────┘          └─────────┬──────────┘
          │                                │
          ▼                                ▼
┌───────────────────┐          ┌────────────────────┐
│ Entraînement ML   │          │ phpMyAdmin         │
│ scikit-learn      │          │ Administration DB  │
└─────────┬─────────┘          └────────────────────┘
          │
          ▼
┌───────────────────┐
│ Modèle ML (.pkl)  │
│ joblib            │
└───────────────────┘

──────────── Streaming (Kafka) ────────────
 Producer → Kafka Topic → Consumer → ETL → DB
```

---

## 3. Organisation du projet

```text
.
├── data/
│   ├── raw/                # Données JSON brutes
│   └── processed/          # Données nettoyées
├── notebooks/
│   └── exploration.ipynb   # Analyse exploratoire
├── scripts/
│   ├── etl.py              # Extraction & transformation
│   ├── create_db.py        # Création DB (ORM)
│   ├── ingest_db.py        # Insertion des données
│   ├── train_model.py      # Entraînement ML
│   ├── producer.py         # Kafka producer
│   └── consumer.py         # Kafka consumer
├── models/
│   └── model.pkl           # Modèle entraîné
├── docker-compose.yml
├── .env
|__ conso.py                # Calcul des consommations CPU, mémoire, etc.
├── requirements.txt
└── README.md
```

---

## 4. Pipeline ETL

### 4.1 Extraction

* Lecture de fichiers JSON structurés
* Support JSON plat et imbriqué (`pd.json_normalize`)

### 4.2 Transformation

* Gestion des valeurs manquantes
* Suppression des doublons
* Conversion des types
* Encodage des variables catégorielles
* Validation du schéma

### 4.3 Chargement

* Sauvegarde JSON nettoyé
* Ingestion dans une base de données relationnelle MySQL/PostgreSQL via SQLAlchemy ORM

---

## 4.4 Base de données relationnelle

* Base **MySQL/PostgreSQL** déployée avec Docker
* Schéma normalisé
* Clé primaire sur l’identifiant métier
* Clé étrangère pour les relations entre les tables
* ORM SQLAlchemy pour l’abstraction SQL

---

## 4.5 Machine Learning

* Modèle supervisé (classification : RandomForest ou Logistic Regression)
* Séparation train / test
* Évaluation par métrique adaptée
* Sauvegarde du modèle avec `joblib`

---

## 4.6 Streaming de données (Kafka)

* Producer : envoie des messages JSON
* Consumer : consomme, valide et ingère
* Gestion des erreurs et duplication possible

---

## 4.7 Variables d’environnement

Les paramètres sensibles (logins de connexion à la base de données, Kafka, chemins) sont gérés via :

* fichier `.env`
* variables Python (`os.environ`)

---

## 4.8 Tests & Robustesse (Pytest)

* Validation du schéma JSON
* Détection des doublons
* Gestion des erreurs d’ingestion
* Scripts réutilisables et modulaires

---
## 4.9 


---
## 4.10 Pistes d’amélioration

* Ajout de tests automatisés avancés
* Monitoring énergétique du pipeline
* Déploiement du modèle en API
* Orchestration avec Airflow
