from P4 import P4,P4Exception
import os
import time

P4_DIRECTORY_PATH=(os.path.split(os.path.realpath(__file__))[0]).replace('\\',"/")
# save this moment as the name of the workspace
WORKSPACE_NAME=time.strftime('%Y_%m_%d_%H_%M_%S')


p4client=WORKSPACE_NAME
# input your port,"ip:port"
p4port="1666"
# input your username
p4user="ljh"
# input your password,P4V's password is not necessary and can be blank
p4password=""

def pull_p4():
    p4 = P4()
    p4.client=p4client
    p4.port=p4port
    p4.user=p4user
    p4.password=p4password    
    client_root=P4_DIRECTORY_PATH+"/P4"
    p4.connect()

    """If the save fails, save again;If the sync fails, sync again,
        sometimes it may fail due to network connectivity reasons
        """
    try:
        client=p4.fetch_client()
        client._root=client_root
        # select mapped area
        client["View"]=["//depot/...  //"+p4client+"/..."]
        p4.save_client(client)
        p4.run_sync('-f')
    except:
        pull_p4(p4client,p4port,p4user,p4password)

if __name__ == "__main__" :
    print('=================start===================')
    pull_p4()
    print('=================end===================')
