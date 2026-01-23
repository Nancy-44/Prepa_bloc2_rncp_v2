# Récupérer un fichier json depuis une API et l'enregistrer localement
import requests
import json
def fetch_json(api_url, local_filename):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Vérifie que la requête a réussi
        data = response.json()  # Parse le contenu JSON de la réponse

        with open(local_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # Enregistre les données JSON dans un fichier local

        print(f"Fichier JSON sauvegardé sous {local_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données: {e}")
    except json.JSONDecodeError as e:
        print(f"Erreur lors du parsing JSON: {e}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier: {e}")

if __name__ == "__main__": 
    api_url = "https://jsonplaceholder.typicode.com/users"
    local_filename = "/home/ubuntu/Bloc2_v2/data/users.json"
    fetch_json(api_url, local_filename)