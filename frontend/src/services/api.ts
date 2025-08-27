import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Adjust the base URL as needed

export const fetchProductInfo = async (image: File) => {
    const formData = new FormData();
    formData.append('file', image);

    try {
        const response = await axios.post(`${API_BASE_URL}/products/recognize`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching product info:', error);
        throw error;
    }
};

export const translateProductInfo = async (text: string, targetLanguage: string) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/translate`, {
            text,
            target_language: targetLanguage,
        });
        return response.data.translated_text;
    } catch (error) {
        console.error('Error translating product info:', error);
        throw error;
    }
};

export const sendMessage = async (message: string, language: string = 'auto', imageData?: string, sessionId?: string) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/chat`, {
            message,
            language,
            image_data: imageData,
            session_id: sessionId, // 新增
        });
        return response.data;
    } catch (error) {
        console.error('Error sending message:', error);
        throw error;
    }
};

// 添加缺少的 fetchMessages 函数
export const fetchMessages = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/chat/messages`);
        return response.data;
    } catch (error) {
        console.error('Error fetching messages:', error);
        throw error;
    }
};