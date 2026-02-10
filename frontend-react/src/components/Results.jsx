
import './Results.css';

function Results({ results, onReset }) {
  const formatCharacterName = (name) => {
    return name
      .replace(/_/g, ' ')
      .split(' ')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  };

  const characterName = formatCharacterName(results.prediction);
  const confidence = (results.confidence * 100).toFixed(2);

  return (
    <div className="result-section">
      <div className="result-header">
        <div className="result-emoji">🎉</div>
        <h2 className="result-title">{characterName}</h2>
        <div className="result-confidence">
          <span className="confidence-label">Confiance :</span>
          <span className="confidence-value">{confidence}%</span>
        </div>
      </div>

      <div className="top-predictions">
        <h3 className="predictions-title">Top 3 Prédictions</h3>
        {results.top_3.map((item, index) => {
          const name = formatCharacterName(item.character);
          const percent = (item.confidence * 100).toFixed(2);
          const medals = ['🥇', '🥈', '🥉'];

          return (
            <div key={index} className="prediction-item">
              <div className="prediction-header">
                <span className="prediction-name">
                  {medals[index]} {name}
                </span>
                <span className="prediction-percent">{percent}%</span>
              </div>
              <div className="prediction-bar">
                <div
                  className="prediction-fill"
                  style={{ width: `${percent}%` }}
                ></div>
              </div>
            </div>
          );
        })}
      </div>

      <button type="button" className="retry-btn" onClick={onReset}>
        <span>🔄</span>
        Tester une autre image
      </button>
    </div>
  );
}

export default Results;