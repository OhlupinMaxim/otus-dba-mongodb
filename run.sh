docker compose -p otus-mongo up -d
docker compose ps mongodb

docker cp create_schema.sh mongodb:/create_schema.sh
docker compose -p otus-mongo exec -it mongodb chown 755 create_schema.sh
docker compose -p otus-mongo exec -it mongodb bash create_schema.sh

