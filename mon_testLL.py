import requests

# Remplace par ta clé d'API Hugging Face
api_key = 'api key'

# URL du modèle Hugging Face
model_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-11B-Vision-Instruct"

# En-tête avec la clé d'API
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Données d'entrée pour le modèle (question mathématique)
data = {
    "inputs": "comment resourdre un equation de premier ordre et donner moi un exemple pour comprends "
}

try:
    # Faire la requête POST pour appeler le modèle
    response = requests.post(model_url, headers=headers, json=data)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Afficher la réponse du modèle
        print("Réponse du modèle :")
        print(response.json())
    else:
        # Afficher l'erreur retournée par l'API
        print(f"Erreur {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    # Gestion des erreurs de réseau
    print(f"Erreur de réseau: {e}")
except Exception as e:
    # Gestion des autres erreurs
    print(f"Une erreur s'est produite: {e}")