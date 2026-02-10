# ============================================================================
# SIMPSONS CHARACTER CLASSIFIER - BACKEND API
# ============================================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import io
from pathlib import Path

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"

CLASSES = [
    'abraham_grampa_simpson',
    'bart_simpson', 
    'charles_montgomery_burns',
    'chief_wiggum',
    'homer_simpson',
    'krusty_the_clown',
    'lisa_simpson',
    'marge_simpson',
    'milhouse_van_houten',
    'moe_szyslak',
    'ned_flanders',
    'principal_skinner',
    'sideshow_bob'
]

IMAGE_SIZE = (224, 224)

print("=" * 80)
print("🚀 DÉMARRAGE DU SERVEUR")
print("=" * 80)

models = {}

try:
    cnn_path = MODELS_DIR / "cnn_scratch.keras"
    models['cnn'] = keras.models.load_model(cnn_path)
    print(f"✅ CNN Scratch chargé : {cnn_path}")
except Exception as e:
    print(f"❌ Erreur chargement CNN : {e}")
    models['cnn'] = None

try:
    eff_path = MODELS_DIR / "efficientnet_final.keras"
    models['efficientnet'] = keras.models.load_model(eff_path)
    print(f"✅ EfficientNet chargé : {eff_path}")
except Exception as e:
    print(f"❌ Erreur chargement EfficientNet : {e}")
    models['efficientnet'] = None

print("=" * 80)

def preprocess_for_cnn(image):
    image = image.resize(IMAGE_SIZE)
    img_array = np.array(image, dtype=np.float32)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def preprocess_for_efficientnet(image):
    from tensorflow.keras.applications.efficientnet import preprocess_input
    image = image.resize(IMAGE_SIZE)
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def preprocess_image(image, model_type):
    if model_type == 'cnn':
        return preprocess_for_cnn(image)
    elif model_type == 'efficientnet':
        return preprocess_for_efficientnet(image)
    else:
        raise ValueError(f"Type de modèle inconnu : {model_type}")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'OK',
        'models_loaded': {
            'cnn': models['cnn'] is not None,
            'efficientnet': models['efficientnet'] is not None
        },
        'classes': len(CLASSES)
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Aucune image fournie'
            }), 400
        
        model_type = request.form.get('model', 'efficientnet')
        
        if model_type not in ['cnn', 'efficientnet']:
            return jsonify({
                'success': False,
                'error': f"Modèle invalide : {model_type}"
            }), 400
        
        if models[model_type] is None:
            return jsonify({
                'success': False,
                'error': f"Le modèle {model_type} n'est pas disponible"
            }), 500
        
        file = request.files['image']
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        print(f"📸 Image reçue : {image.size}, mode: {image.mode}")
        
        img_preprocessed = preprocess_image(image, model_type)
        print(f"✅ Preprocessing {model_type} : {img_preprocessed.shape}")
        
        model = models[model_type]
        predictions = model.predict(img_preprocessed, verbose=0)
        
        top_3_idx = np.argsort(predictions[0])[-3:][::-1]
        
        results = []
        for idx in top_3_idx:
            results.append({
                'character': CLASSES[idx],
                'confidence': float(predictions[0][idx])
            })
        
        print(f"🎯 Prédiction : {results[0]['character']} ({results[0]['confidence']*100:.2f}%)")
        
        return jsonify({
            'success': True,
            'prediction': results[0]['character'],
            'confidence': results[0]['confidence'],
            'top_3': results,
            'model_used': model_type
        })
    
    except Exception as e:
        print(f"❌ Erreur prédiction : {str(e)}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/classes', methods=['GET'])
def get_classes():
    return jsonify({
        'classes': CLASSES,
        'count': len(CLASSES)
    })

if __name__ == '__main__':
    print()
    print("=" * 80)
    print("🎬 SIMPSONS CHARACTER CLASSIFIER API")
    print("=" * 80)
    print()
    print("📡 Serveur démarré sur : http://localhost:5000")
    print("📖 Documentation :")
    print("   - GET  /health     → Status du serveur")
    print("   - POST /predict    → Prédiction d'image")
    print("   - GET  /classes    → Liste des classes")
    print()
    print("🛑 Appuyez sur Ctrl+C pour arrêter")
    print("=" * 80)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)