import React, { useRef } from 'react';

interface ImageUploadButtonProps {
    onImageUpload: (imageDataUrl: string) => void;
}

const ImageUploadButton: React.FC<ImageUploadButtonProps> = ({ onImageUpload }) => {
    const fileInputRef = useRef<HTMLInputElement>(null);

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

    const handleButtonClick = () => {
        fileInputRef.current?.click();
    };

    return (
        <div className="image-upload">
            <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                style={{ display: 'none' }}
            />
            <button 
                type="button" 
                onClick={handleButtonClick}
                className="upload-button"
            >
                📷 Upload Image
            </button>
        </div>
    );
};

export default ImageUploadButton;