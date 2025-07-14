# MP3 to MIDI Converter on Vercel

This repo contains a small Flask application that converts MP3 files to MIDI using the `transkun` CLI. It has been structured for easy deployment to [Vercel](https://vercel.com/).

## Local Development

Run the app locally with:

```bash
pip install -r requirements.txt
python app.py
```

## Deploying to Vercel

The `api/index.py` file exposes the Flask app for Vercel's Python runtime. A `vercel.json` file is included so that deploying with the Vercel CLI will build and route all requests to this serverless function.

```bash
vercel deploy --prod
```

Uploaded files and generated MIDI files are stored in `/tmp` as Vercel functions use ephemeral storage.
