import React, { useState, useRef } from 'react';

interface MessageInputProps {
    onSendMessage: (message: string) => void;
    onImageUpload: (imageDataUrl: string) => void;
}

const MessageInput: React.FC<MessageInputProps> = ({ onSendMessage, onImageUpload }) => {
    const [message, setMessage] = useState('');
    const fileInputRef = useRef<HTMLInputElement>(null);

    const handleSend = (e?: React.FormEvent) => {
        if (e) {
            e.preventDefault(); // 阻止表单提交
        }
        if (message.trim()) {
            onSendMessage(message);
            setMessage('');
        }
    };

    const handleKeyPress = (event: React.KeyboardEvent) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // 阻止默认行为
            handleSend();
        }
    };

    const handleCameraClick = () => {
        fileInputRef.current?.click();
    };

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const imageDataUrl = e.target?.result as string;
                onImageUpload(imageDataUrl);
            };
            reader.readAsDataURL(file);
        }
    };

    return (
        <div className="message-input">
            <form onSubmit={handleSend}>
                <div className="input-container">
                    <input
                        type="text"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="Type your message..."
                    />
                    <button 
                        type="button" 
                        className="camera-button"
                        onClick={handleCameraClick}
                    >
                        📷
                    </button>
                </div>
                <button type="button" className="send-button" onClick={() => handleSend()}>
                    Send
                </button>
                <input
                    ref={fileInputRef}
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                    style={{ display: 'none' }}
                />
            </form>
        </div>
    );
};

export default MessageInput;