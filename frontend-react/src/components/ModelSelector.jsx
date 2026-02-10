
import './ModelSelector.css';

function ModelSelector({ selectedModel, onModelChange }) {
  return (
    <div className="model-selector">
      <div className="section-title">
        <span className="icon">🤖</span>
        Choisissez votre modèle
      </div>
      <div className="model-buttons">
        <button
          type="button"
          className={`model-btn ${selectedModel === 'efficientnet' ? 'active' : ''}`}
          onClick={() => onModelChange('efficientnet')}
        >
          <div className="model-icon">⚡</div>
          <div className="model-name">EfficientNet</div>
        </button>
        <button
          type="button"
          className={`model-btn ${selectedModel === 'cnn' ? 'active' : ''}`}
          onClick={() => onModelChange('cnn')}
        >
          <div className="model-icon">🧠</div>
          <div className="model-name">CNN Scratch</div>
        </button>
      </div>
    </div>
  );
}

export default ModelSelector;