# Run PostgreSQL database in Docker container
docker pull postgres
docker run --name postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres

# OPTIONAL – you may use DBeaver or DataGrip
## install cli
brew uninstall --force postgresql
brew install postgres

## login:pass postgres:postgres
psql -h localhost -p 5432 -U postgres