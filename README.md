# sistemas-operativos








## SEGUNDO PUNTO:


# Sistema de Comunicación por Bus Compartido con Semáforos

## Descripción

Este proyecto simula un sistema de comunicación por bus compartido donde múltiples dispositivos (representados como procesos independientes) compiten por acceder a un canal de comunicación único. La sincronización se gestiona mediante semáforos del módulo `multiprocessing` de Python, garantizando que solo un proceso acceda al bus a la vez y evitando condiciones de carrera.


## Instalación y Configuración

### Paso 1: Crear carpeta y preparar entorno

```
# crear carpeta del proyecto
mkdir bus_compartido && cd bus_compartido

```

### Paso 2: Crear el programa con nano

```
nano main.py

poner el codigo:
#!/usr/bin/env python3
import argparse
import random
import time
from multiprocessing import Process, Semaphore, current_process

def usar_bus(sem: Semaphore, duracion: float, dispositivo: str, intento: int):
    print(f"[{ts()}] {dispositivo} intento {intento}: esperando bus")
    sem.acquire()
    try:
        print(f"[{ts()}] {dispositivo} intento {intento}: usando bus")
        time.sleep(duracion)
        print(f"[{ts()}] {dispositivo} intento {intento}: liberando bus")
    finally:
        sem.release()

def tarea_dispositivo(idx: int, sem: Semaphore, intentos: int, tmin: float, tmax: float):
    dispositivo = f"Dispositivo-{idx}"
    for intento in range(1, intentos + 1):
        # tiempo de “pensar” antes de pedir el bus
        time.sleep(random.uniform(0.1, 0.6))
        duracion = random.uniform(tmin, tmax)
        usar_bus(sem, duracion, dispositivo, intento)
    print(f"[{ts()}] {dispositivo}: terminado")

def ts():
    return time.strftime("%H:%M:%S")

def main():
    parser = argparse.ArgumentParser(
        description="Simulación de bus compartido con semáforo y multiprocessing"
    )
    parser.add_argument("--dispositivos", type=int, default=5, help="cantidad de procesos")
    parser.add_argument("--intentos", type=int, default=3, help="veces que cada proceso usa el bus")
    parser.add_argument("--tmin", type=float, default=0.5, help="uso mínimo del bus en segundos")
    parser.add_argument("--tmax", type=float, default=1.5, help="uso máximo del bus en segundos")
    args = parser.parse_args()

    # semáforo binario: solo 1 proceso en el bus
    sem = Semaphore(1)

    procesos = []
    for i in range(1, args.dispositivos + 1):
        p = Process(target=tarea_dispositivo, args=(i, sem, args.intentos, args.tmin, args.tmax), name=f"Dev-{i}")
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print(f"[{ts()}] Simulación completada")

if __name__ == "__main__":
        main()

```

### Paso 3: Hacer el script ejecutable

```
chmod +x main.py

```


### Paso 4: Ejecutar el programa

```
./main.py

```


## Ejemplo de Salida

```
[16:13:16] Dispositivo-1 intento 1: esperando bus
[16:13:16] Dispositivo-1 intento 1: usando bus
[16:13:16] Dispositivo-2 intento 1: esperando bus
[16:13:16] Dispositivo-4 intento 1: esperando bus
[16:13:16] Dispositivo-5 intento 1: esperando bus
[16:13:16] Dispositivo-3 intento 1: esperando bus
[16:13:17] Dispositivo-1 intento 1: liberando bus
[16:13:17] Dispositivo-2 intento 1: usando bus
[16:13:18] Dispositivo-1 intento 2: esperando bus
[16:13:18] Dispositivo-2 intento 1: liberando bus
[16:13:18] Dispositivo-4 intento 1: usando bus
[16:13:18] Dispositivo-2 intento 2: esperando bus
[16:13:19] Dispositivo-4 intento 1: liberando bus
[16:13:19] Dispositivo-5 intento 1: usando bus
[16:13:19] Dispositivo-4 intento 2: esperando bus
[16:13:19] Dispositivo-5 intento 1: liberando bus
[16:13:19] Dispositivo-3 intento 1: usando bus
[16:13:20] Dispositivo-5 intento 2: esperando bus
[16:13:20] Dispositivo-3 intento 1: liberando bus
[16:13:20] Dispositivo-1 intento 2: usando bus
[16:13:20] Dispositivo-3 intento 2: esperando bus
[16:13:21] Dispositivo-1 intento 2: liberando bus
[16:13:21] Dispositivo-2 intento 2: usando bus
[16:13:21] Dispositivo-1 intento 3: esperando bus
[16:13:22] Dispositivo-2 intento 2: liberando bus
[16:13:22] Dispositivo-4 intento 2: usando bus
[16:13:22] Dispositivo-2 intento 3: esperando bus
[16:13:23] Dispositivo-4 intento 2: liberando bus
[16:13:23] Dispositivo-5 intento 2: usando bus
[16:13:23] Dispositivo-4 intento 3: esperando bus
[16:13:23] Dispositivo-5 intento 2: liberando bus
[16:13:23] Dispositivo-3 intento 2: usando bus
[16:13:24] Dispositivo-5 intento 3: esperando bus
[16:13:24] Dispositivo-3 intento 2: liberando bus
[16:13:24] Dispositivo-1 intento 3: usando bus
[16:13:25] Dispositivo-3 intento 3: esperando bus
[16:13:25] Dispositivo-1 intento 3: liberando bus
[16:13:25] Dispositivo-1: terminado
[16:13:25] Dispositivo-2 intento 3: usando bus
[16:13:26] Dispositivo-2 intento 3: liberando bus
[16:13:26] Dispositivo-2: terminado
[16:13:26] Dispositivo-4 intento 3: usando bus
[16:13:27] Dispositivo-4 intento 3: liberando bus
[16:13:27] Dispositivo-4: terminado
[16:13:27] Dispositivo-5 intento 3: usando bus
[16:13:28] Dispositivo-5 intento 3: liberando bus
[16:13:28] Dispositivo-5: terminado
[16:13:28] Dispositivo-3 intento 3: usando bus
[16:13:28] Dispositivo-3 intento 3: liberando bus
[16:13:28] Dispositivo-3: terminado
[16:13:28] Simulación completada

```

## Evidencias:

<img width="441" height="156" alt="imagen" src="https://github.com/user-attachments/assets/6f3929a6-3678-44a7-ae79-d902298c162a" />


<br>


<img width="490" height="942" alt="imagen" src="https://github.com/user-attachments/assets/59160c35-25c0-4d6c-a1b8-a21ea197a3dc" />

