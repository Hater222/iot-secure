import os, zipfile
from pathlib import Path

required = [
    'app.py','requirements.txt','setup_local_lab.sh','ENTREGA.md',
    'core/uart_sim.py','core/mqtt_sim.py','core/fw_sim.py','core/chain_sim_py.py',
    'pages/1_Amenazas_IoT.py','pages/2_Firmware_y_Contraseñas.py','pages/3_Blockchain_Seguridad.py','pages/4_Auditoria_Entrega.py',
    'tests/test_uart.py','tests/test_mqtt.py','tests/test_fw.py','tests/test_chain_py.py','self_check.py'
]

missing = [f for f in required if not Path(f).exists()]
if missing:
    print('Missing files:', missing)
    raise SystemExit(1)
zipname = 'iot-secure-app.zip'
with zipfile.ZipFile(zipname,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in Path('core').rglob('*'):
        if p.is_file():
            z.write(p, arcname=str(p))
    for p in Path('pages').rglob('*'):
        if p.is_file():
            z.write(p, arcname=str(p))
    for p in Path('tests').rglob('*'):
        if p.is_file():
            z.write(p, arcname=str(p))
    # root files
    for fname in ['app.py','requirements.txt','setup_local_lab.sh','ENTREGA.md','self_check.py','pack_for_students.py','make_zip.sh','teacher_notes.md','prompts_aux.txt']:
        if Path(fname).exists():
            z.write(fname, arcname=fname)
print('Created', zipname)
