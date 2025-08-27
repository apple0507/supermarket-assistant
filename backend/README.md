# Supermarket Assistant Backend

This is the backend for the Supermarket Assistant project, which provides a chatbot interface for users to interact with a supermarket shopping assistant. The backend is built using Python and FastAPI, and it integrates with various services to provide product information, image recognition, and translation capabilities.

## Features

- **Chat Functionality**: Utilizes a GPT model to provide conversational responses to user queries.
- **Product Recognition**: Processes images to identify products and provide detailed information.
- **Multi-language Support**: Translates product information into the user's selected language.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/supermarket-assistant.git
   cd supermarket-assistant/backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Copy the `.env.example` to `.env` and fill in the required variables.

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage Guidelines

- Access the API at `http://localhost:8000`.
- Use the `/chat` endpoint to interact with the chatbot.
- Use the `/products` endpoint to get product information based on image uploads.
- Health check can be performed at `/health`.

## Directory Structure

- `app/`: Contains the main application code.
  - `routers/`: Defines the API routes.
  - `services/`: Contains business logic and integrations.
  - `models/`: Defines data models and schemas.
  - `utils/`: Contains utility functions.

## Testing

To run the tests for the backend, navigate to the `tests/backend` directory and run:

```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.