# Game of Life

Conway's Game of Life implementation with Flask REST API.

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```
The first argument is the name of the module run by python - always "venv" The second one is a name for the new virtual environment

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

To deactivate simply run `deactivate` command both for Windows and Mac/Linux

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application locally

```bash
python endpoints.py
```

The API will be available at `http://localhost:4000`

**Alternatively**:
Run docker engine and pull the image:
```
docker pull krzysiek141/game_of_life:<version>
```

and run the container based on the pulled image. Example:
```
docker run --rm -d -p 5000:4000 --name game_of_life_backend krzysiek141/game_of_life:1.0.0
```
This publishes the app on port 5000 on localhost