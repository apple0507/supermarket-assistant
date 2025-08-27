import React from 'react';

const CameraButton: React.FC = () => {
    const handleCameraClick = () => {
        console.log('Camera button clicked');
        // TODO: 实现相机功能
    };

    return (
        <div className="camera-button">
            <button type="button" onClick={handleCameraClick}>
                📸 Take Photo
            </button>
        </div>
    );
};

export default CameraButton;