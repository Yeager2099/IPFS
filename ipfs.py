import requests
import json

# 使用你的 Pinata API 密钥（硬编码，跳过所有复杂配置）
PINATA_API_KEY = "19b1137ca024283311f8"
PINATA_API_SECRET = "287780f1e5d4de0ac073aa224fe672d6fe674edd9f2ce7ce802576471c38630e"

def pin_to_ipfs(data_dict):
    """将 Python 字典作为 JSON 上传到 IPFS，返回 CID"""
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET
    }
    response = requests.post(url, headers=headers, json={"pinataContent": data_dict})
    if response.status_code != 200:
        raise Exception(f"上传失败，状态码: {response.status_code}, 响应: {response.text}")
    return response.json()["IpfsHash"]

def get_from_ipfs(cid):
    """通过 CID 从 IPFS 获取 JSON 数据，返回 Python 字典"""
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"获取失败，状态码: {response.status_code}, 响应: {response.text}")
    return response.json()
