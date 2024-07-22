

# RapidNotes
RapidNotes is a fast and efficient note-taking application built with FastAPI and MongoDB

## Features
- 🚀 Create, read, update, and delete notes with ease.
- 🎨 Swift and responsive user interface.
- 📦 Integration with MongoDB for reliable data storage.
- ⚡ Built on the powerful FastAPI framework for high-performance APIs.

## Getting Started
### Prerequisites

- Python 3.7 or higher
- [MongoDB](https://www.mongodb.com/try/download/community) installed and running

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/RapidNotes.git
    cd RapidNotes
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Create a `.env` file in the project root and configure your MongoDB connection string:**

    ```env
    MONGODB_URL=mongodb://localhost:27017/rapidnotes
    ```

    Replace `mongodb://localhost:27017/rapidnotes` with your MongoDB connection string.

### Running the Application

```bash
uvicorn main:app --reload
