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

The repository includes a `netlify.toml` configuration that installs the project
dependencies and then starts the Flask application. Netlify provides the port
via the `PORT` environment variable, which the `flask run` command uses.
When setting up your Netlify site you can simply rely on the configuration in
`netlify.toml`, which runs:

```bash
pip install -r requirements.txt && \
FLASK_APP=api/index.py flask run --host=0.0.0.0 --port=$PORT
```

