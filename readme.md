# Game of Life

Conway's Game of Life implementation with Flask REST API.

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

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