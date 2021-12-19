import socket

class port_scan:

    '''Hello Friends , this is the Port scaning script'''
    socket.setdefaulttimeout(0.2)

    def scan():
        target=input('Give me Target Host or IP: ')

        for port in range(1,65536):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=s.connect_ex((target, port))

            if result==0:
                print('{} : {} PORT OPEN ========== -{}-'.format(target, port, socket.getservbyport(port)))
            else:
                print('{} : {} PORT CLOSE <o>'.format(target, port))

#start the program 
start=port_scan.scan()

