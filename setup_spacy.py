import spacy
import sys
import argparse

# -*- coding: utf-8 -*-

def download_spacy_model(model_name="en_core_web_trf"):
    # Vérifier si le modèle est déjà installé
    try:
        nlp = spacy.load(model_name)
        print(f"Le modèle {model_name} est déjà installé.")
        return
    except OSError:
        # Le modèle n'est pas installé, on continue avec le téléchargement
        pass

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
    parser = argparse.ArgumentParser(description="Télécharge et installe un modèle spaCy.")
    parser.add_argument("--model", default="en_core_web_trf", help="Nom du modèle spaCy à installer (par défaut: en_core_web_trf)")
    args = parser.parse_args()

    download_spacy_model(args.model)