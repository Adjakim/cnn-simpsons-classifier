"""
Model Utilities - Fonctions pour la gestion des modèles
"""

import numpy as np
from sklearn.utils.class_weight import compute_class_weight
from typing import Dict


def calculate_class_weights(y_train: np.ndarray) -> Dict[int, float]:
    """
    Calcule les poids des classes pour gérer le déséquilibre
    
    Args:
        y_train: Labels d'entraînement (indices des classes)
    
    Returns:
        Dictionnaire {classe_index: poids}
    """
    classes = np.unique(y_train)
    weights = compute_class_weight(
        class_weight='balanced',
        classes=classes,
        y=y_train
    )
    
    return dict(zip(classes, weights))


def get_model_summary_string(model) -> str:
    """
    Retourne un résumé du modèle sous forme de string
    
    Args:
        model: Modèle Keras
    
    Returns:
        String du résumé
    """
    import io
    stream = io.StringIO()
    model.summary(print_fn=lambda x: stream.write(x + '\n'))
    return stream.getvalue()


def count_trainable_params(model) -> int:
    """
    Compte le nombre de paramètres entraînables
    
    Args:
        model: Modèle Keras
    
    Returns:
        Nombre de paramètres
    """
    return sum([np.prod(v.shape) for v in model.trainable_weights])
