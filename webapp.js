import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

// App Component
const App = () => {
  // State for managing the counter
  const [count, setCount] = React.useState(0);

  // Functions to handle increment and decrement
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count > 0 ? count - 1 : 0);

  return (
    <div style={styles.app}>
      <h1 style={styles.title}>React Counter App</h1>
      <div style={styles.counterBox}>
        <h2 style={styles.counter}>{count}</h2>
        <div style={styles.buttonContainer}>
          <button onClick={increment} style={styles.button}>
            +
          </button>
          <button onClick={decrement} style={styles.button}>
            -
          </button>
        </div>
      </div>
    </div>
  );
};

// Inline Styles
const styles = {
  app: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh',
    backgroundColor: '#f4f4f4',
    fontFamily: 'Arial, sans-serif',
  },
  title: {
    fontSize: '2.5rem',
    margin: '0.5rem',
    color: '#333',
  },
  counterBox: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    margin: '1rem',
  },
  counter: {
    fontSize: '3rem',
    margin: '1rem 0',
  },
  buttonContainer: {
    display: 'flex',
    gap: '1rem',
  },
  button: {
    padding: '0.5rem 1rem',
    fontSize: '1.5rem',
    backgroundColor: '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
};

// Apply hover effect with JavaScript
styles.button[':hover'] = {
  backgroundColor: '#0056b3',
};

// Render App Component
ReactDOM.render(<App />, document.getElementById('root'));
