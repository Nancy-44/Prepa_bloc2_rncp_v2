# create_db.py
import os
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------------------
# 1. Charger les variables d'environnement
# ---------------------------
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")  # Nom du service Docker
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")

# ---------------------------
# 2. Définir l'URL de connexion
# ---------------------------
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------------------------
# 3. Créer le moteur et la session
# ---------------------------
engine = create_engine(DATABASE_URL, echo=True)  # echo=True pour le debug
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ---------------------------
# 4. Définir les tables (exemple User)
# ---------------------------
class User(Base):
    __tablename__ = "users_csv"
    user_id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(50), nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    signup_date = Column(String(50), nullable=False)
    last_login = Column(String(50), nullable=True)
    account_status = Column(String(50), nullable=False)
    monthly_spend = Column(Float)


# ---------------------------
# 5. Créer les tables
# ---------------------------
def init_db():
    print("Création des tables dans la base...")
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès !")

# ---------------------------
# 6. Script principal
# ---------------------------
if __name__ == "__main__":
    init_db()