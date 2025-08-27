import { useEffect, useMemo, useState } from 'react';
import { useState } from 'react';
import { sendMessage } from '../services/api';
import { Message } from '../types';

export const useChat = () => {
    // 初始化时包含助手的欢迎消息
    const [messages, setMessages] = useState<Message[]>([
        {
            id: 'welcome-message',
            text: 'Hello, how can I help you today? 😊',
            sender: 'assistant',
            timestamp: new Date()
        }
    ]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [pendingImage, setPendingImage] = useState<string | null>(null);

    const addImageToChat = (imageDataUrl: string) => {
        // 添加图片到待发送状态
        setPendingImage(imageDataUrl);
        
        // 显示图片消息在聊天中
        const imageMessage: Message = {
            id: Date.now().toString(),
            text: '[Image uploaded]',
            sender: 'user',
            timestamp: new Date(),
            image: imageDataUrl
        };
        setMessages(prevMessages => [...prevMessages, imageMessage]);
    };

    const handleSendMessage = async (messageText: string) => {
        if (!messageText.trim() && !pendingImage) return;
        
        setLoading(true);
        setError(null);
        
        try {
            // 如果有文本消息，添加到聊天
            if (messageText.trim()) {
                const userMessage: Message = {
                    id: Date.now().toString(),
                    text: messageText,
                    sender: 'user',
                    timestamp: new Date()
                };
                setMessages(prevMessages => [...prevMessages, userMessage]);
            }

            // 发送到API（包含图片数据）
            const response = await sendMessage(messageText, 'auto', pendingImage || undefined);
            
            // 添加助手回复
            const botMessage: Message = {
                id: (Date.now() + 1).toString(),
                text: response.response || response.message || 'No response received',
                sender: 'assistant',
                timestamp: new Date()
            };
            
            setMessages(prevMessages => [...prevMessages, botMessage]);
            
            // 清除待发送图片
            setPendingImage(null);
            
        } catch (err) {
            console.error('Chat error:', err);
            setError(err instanceof Error ? err.message : 'Failed to send message');
            
            const errorMessage: Message = {
                id: (Date.now() + 2).toString(),
                text: 'Sorry, I encountered an error. Please try again.',
                sender: 'assistant',
                timestamp: new Date()
            };
            setMessages(prevMessages => [...prevMessages, errorMessage]);
        } finally {
            setLoading(false);
        }
    };

    return { 
        messages, 
        loading, 
        error, 
        sendMessage: handleSendMessage,
        addImageToChat,
        hasPendingImage: !!pendingImage
    };
};