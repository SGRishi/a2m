# MP3 to MIDI Converter

This project provides a small Flask application that converts uploaded MP3 files to MIDI using the [transkun](https://pypi.org/project/transkun/) CLI.

## Running locally

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Flask development server
   ```bash
   FLASK_APP=api/index.py flask run
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000).

## Deploying to Netlify

The repository includes a `netlify.toml` configuration for deploying the Flask app as a serverless function. When setting up your Netlify site, use the following values:

- **Build command:** `pip install -r requirements.txt && cp -r templates api/ && FLASK_APP=api/index.py flask run --host=0.0.0.0 --port=${PORT:-8888}`
- **Functions directory:** `api`

Netlify will build the Python dependencies and deploy the `api/index.py` function. All incoming requests are redirected to this function according to `netlify.toml`.

