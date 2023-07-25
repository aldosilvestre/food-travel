run:
  podman run --name mongo-server -v data:/data/db -p 27017:27017 -d --rm mongodb/mongodb-community-server
build:
  podman build -t mongo-server .
exec:
  podman exec -it mongo-server mongosh
kill:
  podman kill mongo-server
info:
  podman inspect mongo-server
