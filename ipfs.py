import requests
import json

# 硬编码你的Pinata API密钥（避免所有配置文件）
PINATA_API_KEY = "19b1137ca024283311f8"
PINATA_API_SECRET = "287780f1e5d4de0ac073aa224fe672d6fe674edd9f2ce7ce802576471c38630e"

def pin_to_ipfs(data_dict):
    """将字典作为JSON上传到IPFS，返回CID"""
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET
    }
    response = requests.post(url, headers=headers, json={"pinataContent": data_dict})
    return response.json()["IpfsHash"]

def get_from_ipfs(cid):
    """通过CID从IPFS获取JSON，返回字典"""
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    return response.json()
