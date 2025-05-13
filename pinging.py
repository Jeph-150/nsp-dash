# using mock responses to simulate pinging due to network restrictions
mock_responses = {
  "192.168.0.1": 0.034,      # 34ms
  "8.8.8.8": 0.012,          # 12ms
  "10.0.0.1": None,          # unreachable
  "203.0.113.1": 0.087       # 87ms
}

def track_dev(ip):
    response = mock_responses.get(ip)
    if response is None:
        return {"ip": ip, "status": "offline", "response_time": None}
    return {'IP': ip, "status": "online", "response_time": response}

print('-' * 60)
ip = input("Enter IP to ping: ")
result = track_dev(ip)
print(result)
print('-' * 60)

