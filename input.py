import psi4

mol = psi4.geometry("""
  C            0.012220093121    -0.717626540721     0.000000000000
  O           -0.062545506204     0.679938040344     0.000000000000
  H            0.518735639503    -1.098516178616     0.883563931671
  H            0.518735639503    -1.098516178616    -0.883563931671
  H           -1.002097021106    -1.091505681690     0.000000000000
  H            0.811765758420     1.042084199023     0.000000000000
""")

psi4.set_options({'basis': '6-31g*'})

import sys
sys.path.insert(0, './..')
import resp2

psi4.set_module_options('RESP2', {
    'N_VDW_LAYERS'       : 4,
    'VDW_SCALE_FACTOR'   : 1.4,
    'VDW_INCREMENT'      : 0.2,
    'VDW_POINT_DENSITY'  : 1.0,
    'RESP_A'             : 0.01,
    'RESP_B'             : 0.1,
    'CHARGE_GROUPS'      : [1, 2, 3, 6, 4, 5]
    })

e, wfn = psi4.energy('scf', return_wfn=True)
psi4.oeprop(wfn, "MULLIKEN_CHARGES")
psi4.core.plugin('resp2.so', wfn)

