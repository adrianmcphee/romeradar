from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('https://rpc.moonriver.moonbeam.network'))

w3.eth.get_block('latest')

f = open('rome-abi.json')
rome_abi = json.load(f)
rome_contract_address = "0x4a436073552044D5f2f49B176853ad3Ad473d9d6"

rome_contract = w3.eth.contract(address=rome_contract_address, abi=rome_abi)