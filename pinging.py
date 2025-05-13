# using mock responses to simulate pinging due to network restrictions
mock_responses = {
  "192.168.0.1": 0.034,      # 34ms
  "8.8.8.8": 0.012,          # 12ms
  "10.0.0.1": None,          # unreachable
  "203.0.113.1": 0.087       # 87ms
}

print('-' * 60)

ip = input("Enter IP to ping: ")
result = mock_responses.get(ip)

# Handle the mock result
if result is None:
    print(f"{ip} is unreachable.")
else:
    print(f"{ip} is reachable. Response time: {result * 1000:.2f} ms")

print('-' * 60)
input('Press ENTER to exit')
