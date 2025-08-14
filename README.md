# JardasBot


## Building Docker Image

### Mac
To build:

```
docker build -t tower.local:5000/jardas:latest .
```

To run:

```
docker run --rm -v '/path/to/.env:/var/app/.env' -v '/path/to/wordstats.db:/var/app/wordstats.db' --name jardas tower.local:5000/jardas:latest
```

### Mac To Linux

This builds and pushes to the registry in `tower.local`. Note that you need to set the docker daemon to allow insecure registries.
```
docker buildx build --platform linux/amd64 -t tower.local:5000/jardas:latest --push --provenance false --sbom false .
```

Alternatively, we can use a tool like `skopeo` to push the image to the registry:
```
docker buildx build --platform linux/amd64 -t jardas:latest --load .
skopeo copy \
  --dest-tls-verify=false \
  docker-daemon:jardas:latest \
  docker://tower.local:5000/jardas:latest
```