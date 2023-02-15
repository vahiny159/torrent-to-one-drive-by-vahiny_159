import os
import subprocess
import threading
import time

# Installer qbittorent et rclone (mlay e!)
!apt-get update -qq > /dev/null
!apt-get install -qq -y qbittorrent-nox > /dev/null
!wget https://downloads.rclone.org/v1.52.1/rclone-v1.52.1-linux-amd64.deb
!apt install ./rclone-v1.52.1-linux-amd64.deb

# Configuration rclone (replacer l'accès token par votre token, suivez ce lien https://github.com/jakiyaa/rclone-authenticate)
import pexpect

child = pexpect.spawn('rclone config')

child.expect('New remote')

child.sendline('n')

child.expect('name>')

child.sendline('onedrive')

child.expect('Storage> ')

child.sendline('23')

child.expect('client_id')

child.sendline('')

child.expect('client_secret')

child.sendline('')

child.expect('Edit advanced config?')

child.sendline('n')

child.expect('Use auto config?')

child.sendline('n')

child.expect('result>')

child.sendline('{"access_token":"eyJ0eXAiOiJKV1QiLCJub25jZSI6ImdBSTM5R3gzZTZ4LVRqT0l3WVg4STk3ZFNTallJdmU2RWZxLWJEWE03NGsiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC82ZGE2YzA4ZC0xODk3LTRiNTQtOTU3NS01NzQ0YmUwOGY2MzgvIiwiaWF0IjoxNjc2MzgyMTM3LCJuYmYiOjE2NzYzODIxMzcsImV4cCI6MTY3NjM4NzIzMiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQXRab1hWSEQ4RHRicU8vSlBFWE9BOVFjeGZoeWRiVmgzNkFQSldmdW9SZXRlRk5kLzZ2SlRzRjdUSGIyT2FDR1pGQitvbDRzcy8yaCt0elA2MW5Ra1pIbjQxUVZjaC9SenNYL1lLTHFSZmNvPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoicmNsb25lIiwiYXBwaWQiOiJiMTU2NjVkOS1lZGE2LTQwOTItODUzOS0wZWVjMzc2YWZkNTkiLCJhcHBpZGFjciI6IjEiLCJmYW1pbHlfbmFtZSI6InJhemFmaW1haGFuZHJ5IiwiZ2l2ZW5fbmFtZSI6InZhaGlueSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjQxLjc3LjE5LjMwIiwibmFtZSI6InZhaGlueSByYXphZmltYWhhbmRyeSIsIm9pZCI6Ijk1MmY5ZDlhLWZlYTUtNGMxOC1iNDQxLWFiNGY2OWQ1ZDVmNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMjcwREQwMDlEIiwicmgiOiIwLkFYd0FqY0NtYlpjWVZFdVZkVmRFdmdqMk9BTUFBQUFBQUFBQXdBQUFBQUFBQUFDN0FKZy4iLCJzY3AiOiJGaWxlcy5SZWFkIEZpbGVzLlJlYWQuQWxsIEZpbGVzLlJlYWRXcml0ZSBGaWxlcy5SZWFkV3JpdGUuQWxsIFNpdGVzLlJlYWQuQWxsIHByb2ZpbGUgb3BlbmlkIGVtYWlsIiwic3ViIjoibWdvaWh6bWsxRjI5Q3RIUDZjUWFLVHJDSEx4bEhwa2R2Uy1OWnNVVUdXbyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJOQSIsInRpZCI6IjZkYTZjMDhkLTE4OTctNGI1NC05NTc1LTU3NDRiZTA4ZjYzOCIsInVuaXF1ZV9uYW1lIjoidmFoaW55QHg0bWtjLm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6InZhaGlueUB4NG1rYy5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiJzbHBFSVVuWmZVZVIxdWpRX0FFdUFRIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX3N0Ijp7InN1YiI6Im9sd3B6V0Q5emhTSjFtMU9SNjJZU0lzeks4dWx1SnFpMlNwNFNzUnNkRGsifSwieG1zX3RjZHQiOjE2NzU2MzAyNzR9.a498-xxfgj3FmUX_1wgDkl2EKhWWwPCZKvPxjA48rR4znudpcRPe-gQ0U6Li-vaqLapnKwDnsCbnfL-O9xURNb4TnteTO0T5xJdM2-272LwSpfEr5K8vrMRpeUP5AMPC_489mIkhUzhpi3SgCPkjcgMgUBjaaJFzP6MAT_D2ppUM6qtDCkuGW17GB9XZ01Mz85pTimilbINU7GrLv3txC99RgFSON547RooexDGCDIb6gJzazQ49trRu0Q_iEeLnyIDOphAHfUhQCjrPSjvbqRjdG_QQKcJOloIUpZ2y8YleHI_Hph6i5VGEKqhcdIv9hsft6Z7_DNVxoMCnq8kPvQ","token_type":"Bearer","refresh_token":"0.AXwAjcCmbZcYVEuVdVdEvgj2ONllVrGm7ZJAhTkO7Ddq_Vm7AJg.AgABAAEAAAD--DLA3VO7QrddgJg7WevrAgDs_wUA9P96W1fqtvbw9JaU25Ulb4h0lCvCtHMhTN4at8c4GZtDVSXJpCiSAhdmF0LxxCF6fk___e5ouk98da8yiTFLnv_jIyvb-wzZoLvNtGNOHBf2RYccjk0JYTN2tlPfA2mZSA_j11FZjgcNA62Qv3v-RTCaTt-Aq7Nrp15Z9Gm62DROAhtX8llXY92Z5Mhrs6Tmi29uWNN07CmZVk109_KSukCLs-zFQEEio_Ht146FLXUJRvDnIQ3SYG7sFBc5f1Ens6F_bBMA-D_Do1-Ebmq1L3dy4fm6xXzIpY-pames4btZrf_VD5FaYYwOM9ZNkk9IEDE0E50HaTJJs1cAem0iZ1GpwIBRTfqx6JY6Ro7_DWYLsAwnGNq6Ofg9QYyMyvaniAxcnEKVfz4Amsf0KggGjduSOm1H0zOPLf5_SFWVPNKUb_H-_M4ioMLYbq4qmXoQotGMgdF7TFS_7Kmh-UCvNfbsacpgappcFQxhbra6Kim84at4KeupfXwXTRnTCryAoCjkUctnDk7Yp0FSfCB6hfM--k3LZJP6aFDfru4ZUk32AxKEEDNHGFSmpB9cbBISBa1mo7qoWPmQqTjjHjY6NIFZYfNQMvMvoIDPqlZjY92OV04i-vLRD8ntju_ZEFJhNf6tTNEytfPNcZs1dXosFBxAoRAb6gM1aTXPGiupy0jbV9lOnrrgv7gXfuAJ55V3zPqPFxD-LUORAgcMUjqsytoUVun9gNjuTUwCGHIzSUJ4_DEwqXG5xGbmi2NGv4ZVoFDYl8B2V2hNu_86cjXUZU9apirl9ZD00ornbgboBuXVlVlWacUngu8n8KBqfQaHxg9mu4CekTxjIvAXkA","expiry":"2023-02-14T18:07:13.9891593+03:00"}')

child.expect('1 / OneDrive Personal or Business')

child.sendline('1')

child.expect('Chose drive to use')

child.sendline('0')

child.expect('Is that okay?')

child.sendline('y')

child.expect('Yes this is OK')

child.sendline('y')

child.expect('Quit config')

child.sendline('q')

child.wait()

# Mount onedrive

!mkdir onedrive
!nohup rclone --vfs-cache-mode writes mount onedrive: ./onedrive &    

# Install ngrok (Entrer dans le site de ngrok, créer un compte, et recuperer le token)

TOKEN = "1rtb3jOAvQt6yg3FmsGM9Vv2l2x_4eAdaivESTBH5uJMKV9Kc" # Remplacez "your_ngrok_token" par votre token ngrok

def install_ngrok():
    from zipfile import ZipFile
    from urllib.request import urlretrieve
    
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
    urlretrieve(url, 'ngrok-amd64.zip')
    
    with ZipFile('ngrok-amd64.zip', 'r') as zip_ref:
        zip_ref.extractall('/usr/local/bin/')
    os.chmod('/usr/local/bin/ngrok', 0o755)
    os.unlink('ngrok-amd64.zip')

install_ngrok()

if TOKEN != "":
    !ngrok authtoken $TOKEN

# Initialisation de qbittorent (copier le lien et l'ouvrir vers un nouvel ongle, ne pas cliquer dessus)
# Dans l'interface qbittorent changer le chemin de téléchargement par onedrive/votrerepertoire
!mkdir downloads

import threading
import time
import requests
import json
import subprocess


def torrent(port):
    command = subprocess.Popen(['qbittorrent-nox', f'--webui-port={port}'])

def ngrok(port):
    
    ngrok_cmd = subprocess.Popen(['ngrok', 'http', str(port)])    
    localhost_url = "http://localhost:4040/api/tunnels"

    time.sleep(1)
    tunnel_url = requests.get(localhost_url).text
    json_data = json.loads(tunnel_url)

    tunnel_url = json_data['tunnels'][0]['public_url']
    tunnel_url = tunnel_url.replace("https", "http")
    print('Running at localhost: ' + str(port))
    print(tunnel_url)

if __name__ == '__main__':
    
    port = 9999

    thread_torrent = threading.Thread(target = torrent, args=(int(port),))
    thread_ngrok = threading.Thread(target = ngrok, args=(int(port),))

    thread_torrent.start()
    print('Torrent server started!')

    time.sleep(5)
    print('Establishing secure connection!')
    
    thread_ngrok.start()
    print('Secure connection established...')
    print('Username: admin')
    print('password: adminadmin')      
    
    thread_ngrok.join()
    thread_torrent.join()
