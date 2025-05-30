# Dog API Proxy (Flask + Clean Architecture)

This project implements a backend proxy in Flask that exposes a structured and RESTful version of the public [Dog API](https://dogapi.dog/docs/api-v2). It follows the **Proxy Pattern** and principles of **Clean Architecture**, separating routes, business logic, and external data access.

## Project Structure

```
.
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── src/
    ├── proxy/
    │   └── dog_api_proxy.py
    ├── usecases/
    │   └── dog_usecase.py
    └── routes/
        └── dog_routes.py
```

## Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Manuel-Espinosa/api-dog-proxy
   cd api-dog-proxy
   ```

2. **Create Docker network (once):**
   ```bash
   docker network create dog-api-network
   ```

3. Create your .env file 

4. Start the service:
   ```bash
   docker compose up --build
   ```

5. Access the backend at:
   [http://localhost:5000](http://localhost:5000)

## Available Endpoints

- `GET /breeds`
- `GET /breeds/<breed_id>`
- `GET /facts`
- `GET /groups`
- `GET /groups/<group_id>`
- `GET /group-details/<group_id>`
- `GET /group-details/<group_id>/breed/<breed_id>`

## Testing

You can test the RESTful endpoints using the provided `test_endpoints.py` script. Before running it, make sure the backend is up and running:

```bash
docker compose exec dog-api-proxy python test/test_endpoints.py
```

Replace `<breed_id>` and `<group_id>` in the script URLs with real values if needed.

---