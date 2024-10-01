import spacy
import sys

def download_spacy_model():
    model_name = "en_core_web_trf"
    print(f"Téléchargement du modèle spaCy : {model_name}")
    spacy.cli.download(model_name)
    print("Téléchargement terminé.")

    # Vérification de l'installation
    try:
        nlp = spacy.load(model_name)
        print(f"Modèle {model_name} chargé avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement du modèle : {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_spacy_model()