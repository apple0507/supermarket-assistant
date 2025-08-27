import React from 'react';
import Chatbot from './components/Chatbot';
import './App.css';

const App: React.FC = () => {
    return (
        <div className="App">
            <h1>Shopping Assistant</h1>
            <Chatbot />
        </div>
    );
};

export default App;