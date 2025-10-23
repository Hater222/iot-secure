from core.uart_sim import UARTState, handle_cmd
from core.fw_sim import DeviceState, first_boot, gen_keys, sign_image, verify_image, attack_default_creds
from core.chain_sim_py import Ledger, AccessControlPy, ActuatorPy

ok = []
fail = []

def check_uart():
    s = UARTState()
    s.secure = False
    out = handle_cmd(s,'DUMP SECRETS')
    if 'WIFI_PASS' in out:
        ok.append('UART dump insecure')
    else:
        fail.append('UART dump insecure')
    s2 = UARTState()
    s2.pw = 'x'
    s2.secure = True
    handle_cmd(s2,'AUTH bad')
    handle_cmd(s2,'AUTH bad')
    r = handle_cmd(s2,'AUTH bad')
    if 'LOCK' in r or s2.locked:
        ok.append('UART lock on 3 fails')
    else:
        fail.append('UART lock on 3 fails')

def check_fw():
    d = DeviceState()
    if attack_default_creds(d):
        ok.append('FW default creds detected')
    else:
        fail.append('FW default creds detected')
    first_boot(d,'npw')
    if d.first_boot_done and d.admin_hash:
        ok.append('FW first boot')
    else:
        fail.append('FW first boot')
    priv, pub = gen_keys()
    img = b'data'
    sig = sign_image(priv,img)
    if verify_image(pub,img,sig):
        ok.append('FW OTA sign/verify')
    else:
        fail.append('FW OTA sign/verify')

def check_chain():
    L = Ledger()
    eid = L.register('s', b'{}')
    if eid==0:
        ok.append('Ledger register')
    else:
        fail.append('Ledger register')
    ac = AccessControlPy()
    ac.admins.add('prof')
    ac.grant('r','g',60,'prof')
    act = ActuatorPy(ac,L)
    try:
        act.actuate('r','g')
        ok.append('Actuator actuate')
    except Exception:
        fail.append('Actuator actuate')

    try:
        act.actuate('r','bad')
        fail.append('Actuator unauthorized should fail')
    except Exception:
        ok.append('Actuator unauthorized blocked')

check_uart()
check_fw()
check_chain()

print('OK:', ok)
print('FAIL:', fail)
