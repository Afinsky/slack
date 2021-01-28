### BUILD: <br>
```bash
docker build -t serverless -f ./docker/build/main/Dockerfile ./
```

### TEST: <br>
```bash
docker run -it --rm --entrypoint sh serverless
```
or
```bash
docker run -it --rm --entrypoint ls serverless -ls
```

### Create project: <br>
```bash
docker run -it --rm -v $PWD:/app serverless create --template aws-python3
```
or with workspace
```bash
docker run -it --rm -w /app -v $PWD:/app serverless create --template aws-python3
```

### Emulate serverless CLI:
```bash
chmod +x ./sls.sh
./sls.sh --version
```