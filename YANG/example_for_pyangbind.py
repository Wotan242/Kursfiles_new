from interface_config_api import interface_config
import pyangbind.lib.pybindJSON as pybindJSON

int1 = interface_config()

int1.interfaces.interface.add('GigabitEthernet 0/0')
int1.interfaces.interface.add('GigabitEthernet 0/1')

print(pybindJSON.dumps(int1))