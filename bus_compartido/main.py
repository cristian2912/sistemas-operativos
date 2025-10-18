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
