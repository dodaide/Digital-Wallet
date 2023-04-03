# Tài khoản và mật khẩu
USER_NAME = 'admin'
PASSWORD = 'password'

# Địa chỉ người gửi
SENDER_ADDRESS = '0xBf36d47d1a22cBE7fEbF60BA65e77256235b0600'

# Địa chỉ Smart Contract của bạn
CONTRACT_ADDRESS = '0x03b7245dfEf301e50eBd45B5A023092c258f5CF5'

# Private Key
PRIVATE_KEY = "0xc85805c6c5dc0619f35935863beec72aa1d7a2470eeee373797decd30358f063"

# # Khai báo thông tin giao dịch
# SENDER_ADDRESS = '0xABb1Bac369c954dedE76Dce8E23206D849Be625F'

# ABI của Smart Contract của bạn
CONTRACT_ABI = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "true",
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": "true",
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": "false",
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "ETHTransferred",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "recipient",
				"type": "address"
			}
		],
		"name": "transfer",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getSenderBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]