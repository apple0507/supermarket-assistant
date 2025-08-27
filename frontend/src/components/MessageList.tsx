import React from 'react';
import { Message } from '../types';

interface MessageListProps {
    messages: Message[];
}

const MessageList: React.FC<MessageListProps> = ({ messages }) => {
    return (
        <div className="message-list">
            {messages.map((message) => (
                <div key={message.id} className={`message ${message.sender}`}>
                    {message.image && (
                        <img 
                            src={message.image} 
                            alt="Uploaded" 
                            className="message-image"
                        />
                    )}
                    <p>{message.text}</p>
                    <small>{message.timestamp.toLocaleTimeString()}</small>
                </div>
            ))}
        </div>
    );
};

export default MessageList;