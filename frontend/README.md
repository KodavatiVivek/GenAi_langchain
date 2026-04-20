# Frontend setup

This frontend is written in modern Angular using standalone components.

## Scaffold the app

```bash
npm install -g @angular/cli
ng new rag-ui --standalone --routing=false --style=css
```

Then replace the generated `src/` folder with the files inside this `frontend/src/` folder.

## Run

```bash
cd rag-ui
npm install
ng serve
```

The UI expects the FastAPI backend at `http://localhost:8000`.
