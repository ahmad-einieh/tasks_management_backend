# Task Management Backend

A FastAPI/Azure Cosmos DB task-management experiment with user, login, and task routers. `main.py` mounts `/user`, `/auth`, and `/task` and exposes local API documentation at `/docs`.

Install `requirements.txt` in a compatible Python virtual environment, set `COSMOS_ENDPOINT` and `COSMOS_KEY` privately, and run `uvicorn main:app --reload`. `CRUD.py` creates/opens the `tasks` database and user/task containers during import, so use a development Cosmos account with appropriate permissions. Optional mail code requires `SMTP_USERNAME`/`SMTP_PASSWORD`.

Committed cloud credentials were removed; rotate old values. CORS is permissive, and login returns user data rather than establishing comprehensive token-based authorization. Review task ownership/access controls before exposure. Cosmos calls can incur cost. Builds, authentication, and live database/mail behavior were not tested for this documentation refresh.
