Project setup and run instructions for Windows PowerShell

1) Activate the project's virtual environment (per-session):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
D:\projects\cronus\venv\Scripts\Activate.ps1
```

2) Install dependencies (while the venv is active):

```powershell
python -m pip install -r requirements.txt
```

3) Verify imports:

```powershell
python -c "from brainpy import PersonalAI; ai = PersonalAI(); print('Model:', ai.model)"
```

4) Run the Flask app:

```powershell
python app.py
```

Notes:
- The Gemini API requires a `GEMINI_API_KEY` environment variable to be set for generative responses. Create a `.env` file with this variable if you want full functionality.
- Prefer `python -m pip` to ensure you're using the venv pip.
