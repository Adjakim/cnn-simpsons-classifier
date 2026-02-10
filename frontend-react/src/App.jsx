import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import Header from './components/Header';
import ModelSelector from './components/ModelSelector';
import ImageUpload from './components/ImageUpload';
import Results from './components/Results';
import Loading from './components/Loading';

const API_URL = 'http://localhost:5000';

function App() {
  const [selectedModel, setSelectedModel] = useState('efficientnet');
  const [imageFile, setImageFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleModelChange = (model) => {
    setSelectedModel(model);
    console.log('Modèle sélectionné :', model);
  };

  const handleImageUpload = (file) => {
    setImageFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    setResults(null);
    setError(null);
  };

  const handleUrlLoad = async (url) => {
    try {
      const response = await fetch(url);
      const blob = await response.blob();
      const file = new File([blob], 'image.jpg', { type: blob.type });
      setImageFile(file);
      setPreviewUrl(url);
      setResults(null);
      setError(null);
    } catch (err) {
      setError('Impossible de charger l\'image depuis cette URL');
    }
  };

  const handlePredict = async () => {
    if (!imageFile) {
      setError('Aucune image sélectionnée');
      return;
    }

    setIsLoading(true);
    setError(null);
    setResults(null);

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('model', selectedModel);

    try {
      const response = await axios.post(`${API_URL}/predict`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.success) {
        setResults(response.data);
      } else {
        setError(response.data.error || 'Erreur inconnue');
      }
    } catch (err) {
      setError('Erreur de connexion au serveur. Assurez-vous que le backend est lancé.');
      console.error('Erreur prédiction :', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setImageFile(null);
    setPreviewUrl(null);
    setResults(null);
    setError(null);
  };

  return (
    <div className="App">
      {/* Image des Simpsons en coin */}
      <div className="simpsons-corner">
        <img src="/simpsons_family.jpg" alt="The Simpsons Family" />
      </div>

      <div className="container">
        <Header />
        
        <ModelSelector 
          selectedModel={selectedModel} 
          onModelChange={handleModelChange} 
        />

        <ImageUpload
          onImageUpload={handleImageUpload}
          onUrlLoad={handleUrlLoad}
          previewUrl={previewUrl}
          onRemove={handleReset}
          onPredict={handlePredict}
          disabled={isLoading || !imageFile}
        />

        {isLoading && <Loading modelName={selectedModel} />}

        {error && (
          <div className="error-section">
            <div className="error-icon">⚠️</div>
            <h3>Oups ! Une erreur est survenue</h3>
            <p>{error}</p>
            <button className="retry-btn" onClick={handleReset}>
              🔄 Réessayer
            </button>
          </div>
        )}

        {results && <Results results={results} onReset={handleReset} />}
      </div>

      <footer className="footer">
        <p>Développé avec ❤️ par Adja Kimy Fatima</p>
        <p className="footer-tech">
          <span className="tech-badge">React</span>
          <span className="tech-badge">TensorFlow</span>
          <span className="tech-badge">Flask</span>
        </p>
      </footer>
    </div>
  );
}

export default App;