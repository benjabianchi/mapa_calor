# Motion Heatmap

## Correrlo de manera local sin docker

### Instalar ambiente

Puedes usar conda creando un ambiente y instalando el requirements con pip de la siguiente manera:

- conda create -n myenv python=3.7

- conda activate myenv

- pip install -r requirements.txt

### Corre el modelo

- Ubicarse en la carpeta src y usar el comando python para correrlo.

- Tener en cuenta dos  parametros, video y realtime.
    - Video: Path del video, comunmente deberian guardarse en la carpeta data
    - Realtime: Booleano que nos permite indicar si queremos ver el proceso en tiempo real o simplemente no verlo.
        - True: Se ve en tiempo real.
        - False: No se ve en tiemo real.
- Comando ejemplo para correrlo:
    ```
    python motion-heatmap.py --video ../data/input.mp4 --realtime True
    ```
## Correrlo con docker

### Primero crear la imagen
- Ubicarse en la misma altura que el Dockerfile
- Usar el siguiente comando:
```
docker build -t imagen_hm .
```

- Correr la imagen con:

```
docker run -d -v "$PWD/src/motion-heatmap.py":/app/src/motion-heatmap.py -v "$PWD/data":/app/data/ -v "$PWD/output":/app/output imagen_hm
```

- Meternos dentro del contenedor:
    - Primero utiliza el comando *docker ps* para saber la id de nuestro contenedor
    - Luego ingresar al mismo utilizando el comandod docker exec:
        ```
        docker exec -it eb21 /bin/sh
        ```
    - Ya dentro del contenedor podremos correr el archivo .py, debes estar ubicado en el path donde esta el mismo.
        ```
        python3 motion-heatmap.py --video ../data/input.mp4 --realtime False
        ```
