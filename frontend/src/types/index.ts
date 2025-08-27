export interface Product {
    id: string;
    name: string;
    description: string;
    imageUrl: string;
    suitableFor: string[];
    pairWith: string[];
}

export interface Message {
    id: string;
    text: string;
    sender: 'user' | 'assistant';
    timestamp: Date;
    image?: string; // 添加图片字段
}

export interface LanguageOption {
    code: string;
    label: string;
}

export interface ChatState {
    messages: Message[];
    loading: boolean;
    error: string | null;
}