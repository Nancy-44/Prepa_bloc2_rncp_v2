# Projet Bloc 2 – Data Engineer (RNCP)

## Objectif du projet

Ce projet a pour objectif de démontrer la maîtrise des compétences du **Bloc 2 – RNCP Data Engineer** à travers la mise en place d’un pipeline data complet :

* Exploration et préparation de données
* Mise en place d’une base de données relationnelle
* Ingestion et traitement des données
* Entraînement et évaluation d’un modèle de Machine Learning
* Traitement de données en flux avec Kafka
* Tests et assurance qualité
* Analyse de l’impact environnemental

Le projet est conçu pour être **reproductible**, **conteneurisé** et **présentable à un jury**.

---

## Arborescence du projet

```
Bloc2/
│
├── data/
│   ├── raw/                # Données brutes (JSON / CSV)
│   └── processed/          # Données nettoyées
│
├── notebooks/
│   └── exploration.ipynb   # Exploration et analyse des données
│
├── scripts/
│   ├── etl.py              # Extraction, transformation, chargement
│   ├── create_db.py        # Création du schéma via SQLAlchemy ORM
│   ├── ingest_db.py        # Insertion des données en base
│   ├── train_model.py      # Entraînement du modèle ML
│   ├── producer.py         # Producteur Kafka
│   └── consumer.py         # Consommateur Kafka
│
├── models/
│   └── model.joblib        # Modèle ML sauvegardé
│
├── tests/
│   └── test_ingest.py      # Tests unitaires (pytest)
│
|__ imp_eco.py              # Impact écologique
|
├── docker-compose.yml      # Orchestration des services
├── .env                    # Variables d’environnement
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
```

---

## Étape 1 – Exploration des données

* Analyse exploratoire réalisée dans un **notebook Jupyter**
* Données au format **JSON / CSV**
* Identification :

  * valeurs manquantes
  * types de variables
  * variables catégorielles
  * valeurs aberrantes

=> Objectif : comprendre la structure et la qualité des données avant traitement.

---

## Étape 2 – Pipeline ETL

Le script `etl.py` réalise :

* Extraction des données depuis les fichiers sources
* Nettoyage :

  * gestion des valeurs manquantes
  * encodage des variables catégorielles
* Sauvegarde des données transformées

=> Script structuré et réutilisable.

---

## Étape 3 – Base de données PostgreSQL

* Base de données relationnelle **PostgreSQL**
* Déployée via **Docker + docker-compose**
* Administration via **phpMyAdmin**

### ORM

* Utilisation de **SQLAlchemy**
* Définition du schéma logique (tables, clés primaires)
* Création automatique via `create_db.py`

Exemple de schéma de tables : 
Table users :
- id : clé primaire
- age, gender, country, city, email, signup_date, last_login, account_status, monthly_spend : attributs utilisateurs

Table predictions :
- id : clé primaire
- user_id : clé étrangère vers users.id
- prediction : résultat du modèle ML
- created_at : date d’inférence

Explications : La base de données relationnelle repose sur une table users contenant les données brutes issues de l’ingestion.
Une table predictions permet de stocker les résultats du modèle de machine learning.
La relation entre les deux tables est assurée par une clé étrangère (user_id) garantissant l’intégrité référentielle.
Cette architecture permet de séparer les données sources des données calculées, facilitant la maintenance et l’évolutivité du système.

---

## Étape 4 – Ingestion SQL

* Chargement des données nettoyées en base PostgreSQL
* Connexion sécurisée via variables d’environnement
* Vérification de l’intégrité des données

=> Script : `ingest_db.py`

---

## Étape 5 – Machine Learning

* Entraînement d’un modèle avec **scikit-learn**
* Séparation train/test
* Évaluation des performances
* Sauvegarde du modèle avec **joblib**

=> Script : `train_model.py`

---

## Étape 6 – Streaming avec Kafka

* Simulation d’un flux de données
* Producteur Kafka (`producer.py`)
* Consommateur Kafka (`consumer.py`)
* Intégration dans l’architecture dockerisée

=> Objectif : démontrer la capacité à gérer de la donnée en temps réel.

---

## Étape 7 – Tests et qualité

* Tests unitaires avec **pytest**
* Vérifications :

  * conformité du schéma
  * colonnes obligatoires
  * gestion des doublons

=> Dossier : `tests/`

---

## Étape 8 – Impact environnemental

* Estimation de la consommation énergétique du pipeline
* Analyse basée sur :

  * temps de calcul
  * volume de données
  * nombre d’itérations

=> Objectif : sensibilisation à l’écoconception des projets data.

---

## Lancement du projet

```bash
# Lancer les services
docker-compose up -d --build

# Créer la base
python3 scripts/create_db.py

# ETL
python3 scripts/etl.py

# Ingestion
python3 scripts/ingest_db.py

# Entraînement ML
python3 scripts/train_model.py

# Tests
pytest tests/test_ingest.py

---

## Améliorations possibles

* Déploiement cloud
* Orchestration avec Airflow (planification automatisée des tâches via un DAG)
* Monitoring (Prometheus / Grafana)
* CI/CD pour le déploiement continu et reproductible

---

## Auteur : Nancy Frémont

Projet réalisé dans le cadre de la **préparation à la certification RNCP – Data Engineer (Bloc 2)**.