"""
Data Utilities - Fonctions pour la gestion des données
"""

import os
import numpy as np
from pathlib import Path
from PIL import Image
from typing import List, Tuple, Dict
import shutil
from tqdm import tqdm


def count_images_in_directory(directory: Path) -> Dict[str, int]:
    """
    Compte le nombre d'images dans chaque sous-dossier
    
    Args:
        directory: Chemin du dossier parent
    
    Returns:
        Dictionnaire {nom_classe: nombre_images}
    """
    counts = {}
    
    for class_dir in directory.iterdir():
        if class_dir.is_dir():
            extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
            count = sum(1 for f in class_dir.iterdir() 
                       if f.suffix in extensions)
            counts[class_dir.name] = count
    
    return counts


def verify_image(image_path: Path) -> bool:
    """
    Vérifie si une image est valide et peut être ouverte
    
    Args:
        image_path: Chemin de l'image
    
    Returns:
        True si l'image est valide, False sinon
    """
    try:
        with Image.open(image_path) as img:
            img.verify()
        return True
    except Exception:
        return False


def get_image_statistics(image_path: Path) -> Dict:
    """
    Calcule les statistiques d'une image
    
    Args:
        image_path: Chemin de l'image
    
    Returns:
        Dictionnaire avec width, height, mode, size
    """
    try:
        with Image.open(image_path) as img:
            return {
                'width': img.width,
                'height': img.height,
                'mode': img.mode,
                'size': os.path.getsize(image_path)
            }
    except Exception:
        return None


def stratified_sample(
    source_dir: Path,
    n_samples: int,
    stratify_by: str = 'brightness'
) -> List[Path]:
    """
    Échantillonnage stratifié des images
    
    Args:
        source_dir: Dossier source contenant les images
        n_samples: Nombre d'images à échantillonner
        stratify_by: Critère de stratification ('brightness', 'size', etc.)
    
    Returns:
        Liste des chemins d'images sélectionnées
    """
    # TODO: Implémenter l'échantillonnage stratifié
    # Pour l'instant, retourne un échantillonnage aléatoire
    import random
    
    all_images = list(source_dir.glob('*.jpg')) +                  list(source_dir.glob('*.jpeg')) +                  list(source_dir.glob('*.png'))
    
    if len(all_images) <= n_samples:
        return all_images
    
    return random.sample(all_images, n_samples)
