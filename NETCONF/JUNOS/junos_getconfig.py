#!/usr/bin/env python3

from ncclient import manager
from lxml import etree
from ncclient.operations.rpc import RPCError


def main():
    with manager.connect(host='192.168.181.51',
                         port=830,
                         username='lab',
                         password='lab123',
                         hostkey_verify=False,
                         device_params={'name': 'junos'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as junos_nc:

        f1 = '''
        <configuration>    
             <system>
                 <host-name/>
             </system> 
        </configuration>
        

        '''

       
       
       

        try:
            #oc_resp = junos_nc.get_config('running')
            oc_resp = junos_nc.get_config('running',
                                              filter=('subtree', f1))
            print(oc_resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()
