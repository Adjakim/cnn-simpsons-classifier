"""
Visualization Utilities - Fonctions pour les visualisations
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import List, Optional
from pathlib import Path


def plot_class_distribution(
    counts: dict,
    title: str = "Distribution des Classes",
    save_path: Optional[Path] = None
):
    """
    Affiche un graphique en barres de la distribution des classes
    
    Args:
        counts: Dictionnaire {classe: nombre}
        title: Titre du graphique
        save_path: Chemin de sauvegarde (optionnel)
    """
    plt.figure(figsize=(14, 6))
    
    classes = list(counts.keys())
    values = list(counts.values())
    
    # Créer le graphique
    bars = plt.bar(range(len(classes)), values, color='steelblue', alpha=0.8)
    
    # Ajouter les valeurs sur les barres
    for i, (bar, value) in enumerate(zip(bars, values)):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                f'{value}', ha='center', va='bottom', fontsize=10)
    
    plt.xlabel('Classes (Personnages)', fontsize=12)
    plt.ylabel('Nombre d'images', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(range(len(classes)), classes, rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_images_grid(
    images: List,
    labels: List,
    predictions: Optional[List] = None,
    n_cols: int = 5,
    figsize: tuple = (15, 10),
    save_path: Optional[Path] = None
):
    """
    Affiche une grille d'images avec leurs labels
    
    Args:
        images: Liste d'images (numpy arrays)
        labels: Liste de labels
        predictions: Liste de prédictions (optionnel)
        n_cols: Nombre de colonnes
        figsize: Taille de la figure
        save_path: Chemin de sauvegarde (optionnel)
    """
    n_images = len(images)
    n_rows = (n_images + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.flatten() if n_images > 1 else [axes]
    
    for idx, ax in enumerate(axes):
        if idx < n_images:
            ax.imshow(images[idx])
            
            title = f"True: {labels[idx]}"
            if predictions and idx < len(predictions):
                title += f"\nPred: {predictions[idx]}"
                color = 'green' if labels[idx] == predictions[idx] else 'red'
                ax.set_title(title, color=color, fontsize=8)
            else:
                ax.set_title(title, fontsize=8)
            
            ax.axis('off')
        else:
            ax.axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_training_history(
    history: dict,
    save_path: Optional[Path] = None
):
    """
    Visualise l'historique d'entraînement
    
    Args:
        history: Dictionnaire d'historique Keras
        save_path: Chemin de sauvegarde (optionnel)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Accuracy
    ax1.plot(history['accuracy'], label='Train Accuracy', linewidth=2)
    ax1.plot(history['val_accuracy'], label='Val Accuracy', linewidth=2)
    ax1.set_xlabel('Epoch', fontsize=12)
    ax1.set_ylabel('Accuracy', fontsize=12)
    ax1.set_title('Model Accuracy', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Loss
    ax2.plot(history['loss'], label='Train Loss', linewidth=2)
    ax2.plot(history['val_loss'], label='Val Loss', linewidth=2)
    ax2.set_xlabel('Epoch', fontsize=12)
    ax2.set_ylabel('Loss', fontsize=12)
    ax2.set_title('Model Loss', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
