import './Loading.css';

function Loading({ modelName }) {
  const displayName = modelName === 'efficientnet' ? 'EfficientNet' : 'CNN Scratch';
  
  return (
    <div className="loading">
      <div className="spinner"></div>
      <p>Analyse en cours avec <span className="model-name">{displayName}</span>...</p>
    </div>
  );
}

export default Loading;