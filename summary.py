from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('https://rpc.moonriver.moonbeam.network'))

w3.eth.get_block('latest')

f = open('rome-abi.json')
romeabi = json.load(f)

