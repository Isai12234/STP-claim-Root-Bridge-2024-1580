# STP Claim Root Bridge Attack - Scapy

## Autor
Nombre: Juan isai Casado De oleo
Matrícula: 2024-1580

---

## Objetivo
Desarrollar un script en Python utilizando Scapy para enviar BPDUs manipuladas con prioridad 0 con el fin de convertirse en el Root Bridge en una red con STP habilitado.

---

## Topología
- Router
- Switch con STP habilitado
- Host atacante (Kali Linux)
- Host víctima  (Window 10)

---

## Funcionamiento
El script envía BPDUs falsas con prioridad 0 cada 2 segundos para forzar al switch a elegir al atacante como Root Bridge.

---

## Parámetros
- Interfaz: ens3
- Prioridad: 0
- MAC falsa: 00:00:00:00:00:01

---

## Mitigación
- BPDU Guard
- Root Guard
- PortFast
- Configuración manual de prioridad STP
