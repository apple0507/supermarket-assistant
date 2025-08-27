# Supermarket Shopping Assistant

This project is a Supermarket Shopping Assistant designed to help users find product information, view real-time images of products, and translate product details into their preferred language.

## Project Structure

The project is divided into two main parts: the frontend and the backend.

### Frontend

The frontend is built using React and provides a chatbot interface for user interactions. It includes features such as:

- Image upload and camera functionality for product recognition.
- A language selector for translating product information.

#### Key Files

- `src/main.tsx`: Entry point for the React application.
- `src/App.tsx`: Main application component.
- `src/components/`: Contains reusable components like Chatbot, MessageList, MessageInput, ImageUploadButton, CameraButton, and LanguageSelector.
- `src/services/api.ts`: Handles API calls to the backend.

### Backend

The backend is developed using Python and FastAPI. It provides the necessary APIs for the frontend to interact with the product recognition and translation services.

#### Key Files

- `app/main.py`: Entry point for the backend application.
- `app/routers/`: Contains routes for chat, product information, and health checks.
- `app/services/`: Implements functionalities for interacting with the GPT model, processing images, retrieving product information, and translating text.
- `app/models/schemas.py`: Defines data models for request and response validation.

## Setup Instructions

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies using npm:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm run start
   ```

### Backend

1. Navigate to the `backend` directory.
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```
   uvicorn app.main:app --reload
   ```

## Usage Guidelines

- Use the chatbot interface to interact with the shopping assistant.
- Upload images of products or use the camera to capture images for recognition.
- Select your preferred language from the dropdown to translate product information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.