import network
sta_if = network.WLAN(network.STA_IF)
def do_connect(ssid,password):
    if not sta_if.isconnected():
        print('connecting to network...')
        try:
            sta_if.active(True)
            sta_if.connect(ssid, password)
        except:
            print('Cannot connect')
#        while not sta_if.isconnected():
#            pass
    print('Connection Successfull')

def do_disconnect():
    sta_if.active(False)
    print(sta_if.isconnected())
    sta_if.active(True)

def ifconfig():
    print("--------------------------")
    print("Network Information")
    print("--------------------------")
    info = sta_if.ifconfig()
    if sta_if.isconnected():
        print("<BROADCASTING>")
    else:
        print("<>")
    print("--------------------------")
    print("Access Point Name: "+str(sta_if.config('essid')))
    print("Access Point MAC Address: "+str(sta_if.config('mac')))
    print("--------------------------")
    print("Your Device IP: "+info[0])
    print("Subnet Mask: "+info[1])
    print("Gateway: "+info[2])
    print("DNS: "+info[3])
    

def do_show():
    print("Available WLANs")
    wlans = sta_if.scan()
    for i in wlans:
        print(str(i[0]))

def do_on():
    sta_if.active(True)

def do_off():
    sta_if.active(False)

def do_status():
    status_code = sta_if.status()
    if status_code == 1000:
        print("No Connection and No Activities")
    elif status_code == 1001:
        print("Connecting")
    elif status_code == 202:
        print("Failed due to password error")
    elif status_code == 201:
        print("Failed, because there is no access point reply")
    elif status_code == 1010:
        print("Connected")
    elif status_code == 203:
        print("Failed")
    elif status_code == 200:
        print("Timeout")
    elif status_code == 204:
        print("Handshake timeout")