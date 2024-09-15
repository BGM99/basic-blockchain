import datetime as date
import sys
import time

import service

from block import Block
from blockchain import Blockchain
from crypto import Wallet
from node import Node
import socket

import logging
import sys


#wallet = Wallet()
#wallet.generate_key_pair()

blockchain = Blockchain()
blockchain.load_from_file()
#blockchain.create_genesis_block(wallet.public_key_pem, wallet.private_key_pem)
#block = Block(date.datetime.now(), ("56c9ac4d6090de", 1), "", wallet.public_key_pem)
#blockchain.add_block(block, wallet.private_key_pem)


# Logger konfigurieren
logger = logging.getLogger('kademlia')
logger.setLevel(logging.DEBUG)  # Log Level: DEBUG, INFO, WARNING, ERROR, CRITICAL

# StreamHandler für die Docker-Konsole (stdout)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Format für den Logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Hinzufügen des Handlers zum Logger
logger.addHandler(console_handler)

# Beispiel-Logs
#logger.debug('This is a debug message')
#logger.info('This is an info message')
#logger.warning('This is a warning message')
#logger.error('This is an error message')
#logger.critical('This is a critical message')


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
logger.warning("IP Address: " + ip_address)

if len(sys.argv) > 1:
    node = Node(logger, ip_address, sys.argv[1])
    logger.warning("Started Node with " + sys.argv[1])
else:
    node = Node(logger, ip_address)
    logger.warning("Starting network ... ")

service.start_api_service()

logger.warning("Started api service")

# Print the contents of the blockchain
for block in blockchain.chain:
    print(f"Block #: {block.index}")
    print(f"previous_hash: {block.previous_hash}")
    print(f"timestamp: {block.timestamp}")
    print(f"data: {block.data}")
    print(f"person_public_key: {block.person_public_key}")
    print(f"validator_public_key: {block.validator_public_key}")
    print(f"signature: {block.signature}")
    print(f"hash: {block.hash}")
    print("\n")

time.sleep(9999)  # Check every second
