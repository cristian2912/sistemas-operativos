# SISTEMAS OPERATIVOS






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


# Parte 3 — Implementación de RAID en **VirtualBox** (RAID0, RAID1, RAID5)

Esta guía cumple la **Parte tres** del parcial: implementar **RAID 1** y **RAID 5**. Incluye también **RAID 0** para contraste. Se realiza dentro de una **VM en VirtualBox** usando Linux y **mdadm**.

---

## 0) Requisitos

- VirtualBox instalado en el host.
- ISO de Ubuntu Server o Desktop (22.04+ recomendado).
- VM creada con **1 disco del SO** y **discos adicionales vacíos** para cada RAID:
  - RAID0: 3 discos de datos (ej. 3 × 2 GB).
  - RAID1: 2 discos de datos (ej. 2 × 2 GB).
  - RAID5: 3 discos de datos (ej. 3 × 2 GB).

> Puedes reutilizar discos entre niveles si haces pruebas por separado. Lo claro es que **cada arreglo** necesita el número mínimo de discos indicado.

---

## 1) Añadir discos en VirtualBox

### Opción GUI
1. Apaga la VM si está encendida.
2. **Configuración → Almacenamiento → Controladora SATA → Añadir disco duro**.
3. Crea discos **VHD/VDI** de tamaño fijo o dinámico (2 GB es suficiente para pruebas).
4. Añade los discos requeridos para cada arreglo.

### Opción CLI (host)
```bash
# ejemplo: crear 3 discos de 2 GB para RAID0
VBoxManage createmedium disk --filename "$HOME/VirtualBox VMs/VM-SO/raid0-disk1.vdi" --size 2048
VBoxManage createmedium disk --filename "$HOME/VirtualBox VMs/VM-SO/raid0-disk2.vdi" --size 2048
VBoxManage createmedium disk --filename "$HOME/VirtualBox VMs/VM-SO/raid0-disk3.vdi" --size 2048
# adjuntar a la VM
VBoxManage storageattach "VM-SO" --storagectl "SATA" --port 1 --device 0 --type hdd --medium "$HOME/VirtualBox VMs/VM-SO/raid0-disk1.vdi"
VBoxManage storageattach "VM-SO" --storagectl "SATA" --port 2 --device 0 --type hdd --medium "$HOME/VirtualBox VMs/VM-SO/raid0-disk2.vdi"
VBoxManage storageattach "VM-SO" --storagectl "SATA" --port 3 --device 0 --type hdd --medium "$HOME/VirtualBox VMs/VM-SO/raid0-disk3.vdi"
```

---

## 2) Preparación dentro de la VM (Ubuntu)

Inicia la VM e instala mdadm:
```bash
sudo apt update
sudo apt install -y mdadm
```

Identifica los discos nuevos:
```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
# típicamente verás /dev/sdb, /dev/sdc, /dev/sdd, etc.
```

> Para pruebas puedes usar el **disco entero**. Si prefieres particionar: `sudo parted /dev/sdb --script mklabel gpt mkpart primary 1MiB 100%` y luego usa `/dev/sdb1` en los comandos.

---

## 3) RAID 0 (rendimiento, sin tolerancia a fallos)

Crear arreglo con 3 discos (ajusta nombres si difieren):
```bash
sudo mdadm --create /dev/md0 --level=0 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd
watch -n1 cat /proc/mdstat     # espera a que esté activo (UUU)
```

Formatear y montar:
```bash
sudo mkfs.ext4 /dev/md0
sudo mkdir -p /mnt/raid0
sudo mount /dev/md0 /mnt/raid0
df -h | grep md0
```

Prueba rápida:
```bash
sudo sh -c 'head -c 200M </dev/urandom > /mnt/raid0/test.bin'
sha256sum /mnt/raid0/test.bin
```

Falla esperada si quitas un disco:
```bash
# simular fallo de /dev/sdc
sudo mdadm /dev/md0 --fail /dev/sdc --remove /dev/sdc
cat /proc/mdstat   # el arreglo queda dañado (RAID0 no tolera fallos)
```

---

## 4) RAID 1 (espejo, tolera la falla de 1 disco)

Crear arreglo con 2 discos:
```bash
sudo mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sde /dev/sdf
watch -n1 cat /proc/mdstat   # espera sincronización (UU)
```

Formatear y montar:
```bash
sudo mkfs.ext4 /dev/md1
sudo mkdir -p /mnt/raid1
sudo mount /dev/md1 /mnt/raid1
```

Simular fallo y verificar servicio activo:
```bash
sudo mdadm /dev/md1 --fail /dev/sde
cat /proc/mdstat        # [U_]  uno en fallo
sudo mdadm --detail /dev/md1
# sigue montado y accesible con 1 disco
```

Reemplazo / reconstrucción:
```bash
# desasociar el fallado y añadir un disco nuevo /dev/sdg (añadirlo desde VirtualBox si no existe)
sudo mdadm /dev/md1 --remove /dev/sde
sudo mdadm /dev/md1 --add /dev/sdg
watch -n1 cat /proc/mdstat   # reconstrucción hasta volver a (UU)
```

---

## 5) RAID 5 (paridad, tolera la falla de 1 disco)

Crear arreglo con 3 discos:
```bash
sudo mdadm --create /dev/md5 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd
watch -n1 cat /proc/mdstat   # ver sincronización (UUU)
```

Formatear y montar:
```bash
sudo mkfs.ext4 /dev/md5
sudo mkdir -p /mnt/raid5
sudo mount /dev/md5 /mnt/raid5
```

Simular fallo y reconstruir:
```bash
sudo mdadm /dev/md5 --fail /dev/sdc
sudo mdadm /dev/md5 --remove /dev/sdc
# añade un disco nuevo /dev/sdg desde VirtualBox si hace falta
sudo mdadm /dev/md5 --add /dev/sdg
watch -n1 cat /proc/mdstat   # reconstrucción hasta (UUU)
```

---

## 6) Persistencia en reinicio

Generar config y entradas en fstab:
```bash
# guardar definición de arreglos
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
sudo update-initramfs -u

# obtener UUID del sistema de archivos
sudo blkid /dev/md0
sudo blkid /dev/md1
sudo blkid /dev/md5

# añadir a /etc/fstab (ejemplo para md0)
echo 'UUID=<uuid-md0> /mnt/raid0 ext4 defaults,nofail 0 0' | sudo tee -a /etc/fstab
echo 'UUID=<uuid-md1> /mnt/raid1 ext4 defaults,nofail 0 0' | sudo tee -a /etc/fstab
echo 'UUID=<uuid-md5> /mnt/raid5 ext4 defaults,nofail 0 0' | sudo tee -a /etc/fstab
```

---

## 7) Verificación rápida

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
sudo mdadm --detail /dev/md1
sudo mdadm --detail /dev/md5
```

---

## 8) Transcripción de terminal (ejemplo)


<img width="737" height="173" alt="imagen" src="https://github.com/user-attachments/assets/17b13528-771c-4ac2-a7d2-37eb7e3559d9" />


<img width="807" height="98" alt="imagen" src="https://github.com/user-attachments/assets/c4dff716-db26-41a2-a144-d08c62f41c84" />

<img width="793" height="48" alt="imagen" src="https://github.com/user-attachments/assets/93e987fb-29fe-418e-a6de-e0e65353822b" />

<img width="793" height="27" alt="imagen" src="https://github.com/user-attachments/assets/1142e93a-e250-47b2-883a-e0c468bec090" />

<img width="793" height="27" alt="imagen" src="https://github.com/user-attachments/assets/e411fcc3-162c-45ed-81d3-a0220f969c38" />

<img width="793" height="51" alt="imagen" src="https://github.com/user-attachments/assets/57f20920-9ad3-4462-9445-bf4afda687d8" />

<img width="793" height="51" alt="imagen" src="https://github.com/user-attachments/assets/780faca8-3f0c-4490-90a3-d3a9cf98a300" />

# RAID0 sin tolerancia: degradado/dañado

<img width="793" height="51" alt="imagen" src="https://github.com/user-attachments/assets/594ca7ee-0698-4e5b-adc6-c7a7126b7525" />
# ... sincroniza a (UU) y funciona con 1 disco fallado ...

<img width="793" height="51" alt="imagen" src="https://github.com/user-attachments/assets/3a88089d-d4c3-4abb-bd58-33c822871a1d" />
# ... sincroniza a (UUU). Falla 1 disco, se reconstruye tras añadir reemplazo ...

---

## 9) Notas de evaluación
- RAID0: rendimiento. **No** tolera fallas.
- RAID1: espejo. Tolerancia a **1** disco.
- RAID5: paridad distribuida. Tolerancia a **1** disco.
- Usa `mdadm --detail --scan` y capturas de `cat /proc/mdstat` como evidencia.
