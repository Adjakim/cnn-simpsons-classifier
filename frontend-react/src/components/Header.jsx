
import './Header.css';

function Header() {
  return (
    <div className="header">
      <h1 className="title">
        <span className="emoji">🎬</span>
        Simpsons Character Classifier
      </h1>
      <p className="tagline">
        "D'oh! Qui est ce personnage ? Laissez notre IA le découvrir !"
      </p>
    </div>
  );
}

export default Header;