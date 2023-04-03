from web3 import Web3
from config import *

# Kết nối với mạng Ethereum
web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Kiểm tra xem kết nối đã thành công chưa
if web3.is_connected():
    print("Kết nối đến mạng Ethereum thành công")
else:
    print("Kết nối đến mạng Ethereum thất bại")
    exit()

contractAddress = Web3.to_checksum_address(CONTRACT_ADDRESS)
contractAbi = CONTRACT_ABI
# Tạo đối tượng Smart Contract từ địa chỉ và ABI của Smart Contract
contract = web3.eth.contract(address=contractAddress, abi=contractAbi)

def getBalance():
    # Số dư còn lại
    senderBalance = contract.functions.getSenderBalance().call()
    return round(web3.from_wei(senderBalance, 'ether'), 2)

def transact(receiverAddress, tokenAmount):
    # Khai báo thông tin giao dịch
    privateKey = PRIVATE_KEY
    senderAddress = SENDER_ADDRESS
    print("Địa chỉ của bạn: ", senderAddress)

    # Triển khai giao dịch
    try:
        transaction = contract.functions.transfer(receiverAddress).build_transaction({
            'from': senderAddress,
            'nonce': web3.eth.get_transaction_count(senderAddress),
            'value': web3.to_wei(tokenAmount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei')
        })

        # Ký và gửi giao dịch
        signed_txn = web3.eth.account.sign_transaction(transaction, privateKey)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print("Hash: ", web3.to_hex(tx_hash))
        return True
    except:
        return False

