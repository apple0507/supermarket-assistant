import React from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import { useChat } from '../hooks/useChat';

const Chatbot: React.FC = () => {
    const { messages, sendMessage, addImageToChat, hasPendingImage } = useChat();

    return (
        <div className="chatbot">
            <MessageList messages={messages} />
            <MessageInput 
                onSendMessage={sendMessage} 
                onImageUpload={addImageToChat}
            />
            {hasPendingImage && (
                <p style={{ color: '#1e3a8a', fontSize: '14px', textAlign: 'center' }}>
                    📷 Image ready to send - add your message and click Send
                </p>
            )}
        </div>
    );
};

export default Chatbot;