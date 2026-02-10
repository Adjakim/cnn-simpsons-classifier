import { useState, useRef } from 'react';
import './ImageUpload.css';

function ImageUpload({ onImageUpload, onUrlLoad, previewUrl, onRemove, onPredict, disabled }) {
  const [activeTab, setActiveTab] = useState('upload');
  const [urlInput, setUrlInput] = useState('');
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type.startsWith('image/')) {
      onImageUpload(file);
    } else {
      alert('Veuillez sélectionner une image valide (PNG, JPG, JPEG)');
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
      onImageUpload(file);
    } else {
      alert('Veuillez déposer une image valide (PNG, JPG, JPEG)');
    }
  };

  const handleUrlSubmit = () => {
    if (!urlInput.trim()) {
      alert('Veuillez entrer une URL');
      return;
    }
    onUrlLoad(urlInput);
  };

  return (
    <div className="upload-section">
      <div className="section-title">
        <span className="icon">📸</span>
        Chargez votre image
      </div>

      {/* Tabs */}
      <div className="tabs">
        <button
          type="button"
          className={`tab ${activeTab === 'upload' ? 'active' : ''}`}
          onClick={() => setActiveTab('upload')}
        >
          📁 Upload
        </button>
        <button
          type="button"
          className={`tab ${activeTab === 'url' ? 'active' : ''}`}
          onClick={() => setActiveTab('url')}
        >
          🔗 URL
        </button>
      </div>

      {/* Upload Tab */}
      {activeTab === 'upload' && (
        <div className="tab-content">
          <div
            className={`upload-area ${isDragging ? 'dragover' : ''}`}
            onClick={() => fileInputRef.current.click()}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
          >
            <h3>Glissez une image ou cliquez</h3>
            <p>PNG, JPG, JPEG (max 10 MB)</p>
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              style={{ display: 'none' }}
            />
          </div>
        </div>
      )}

      {/* URL Tab */}
      {activeTab === 'url' && (
        <div className="tab-content">
          <div className="url-input-container">
            <input
              type="text"
              className="url-input"
              placeholder="https://exemple.com/homer.jpg"
              value={urlInput}
              onChange={(e) => setUrlInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleUrlSubmit()}
            />
            <button type="button" className="url-btn" onClick={handleUrlSubmit}>
              <span className="btn-icon">🔗</span>
              Charger
            </button>
          </div>
        </div>
      )}

      {/* Preview */}
      {previewUrl && (
        <div className="preview-section">
          <div className="section-title">
            <span className="icon">👁️</span>
            Prévisualisation
          </div>
          <div className="preview-container">
            <img src={previewUrl} alt="Preview" className="preview-image" />
            <button type="button" className="remove-btn" onClick={onRemove}>
              <span>✕</span>
            </button>
          </div>
        </div>
      )}

      {/* Predict Button */}
      {previewUrl && (
        <button
          type="button"
          className="predict-btn"
          onClick={onPredict}
          disabled={disabled}
        >
          <span className="btn-icon">🔮</span>
          <span className="btn-text">Identifier le personnage</span>
        </button>
      )}
    </div>
  );
}

export default ImageUpload;
