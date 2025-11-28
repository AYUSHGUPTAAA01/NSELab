# -*- coding: utf-8 -*-
import hashlib
import time
import hmac
import random

shared_secret = "network_secret_key"
client_id = "client_01"

def generate_nonce():
    return str(random.randint(100000, 999999))

def hash_response(nonce, secret, client):
    return hmac.new(secret.encode(), (nonce + client).encode(), hashlib.sha256).hexdigest()

nonce = generate_nonce()
print("Server sends nonce to client:", nonce)

client_response = hash_response(nonce, shared_secret, client_id)
print("Client sends encrypted response:", client_response)

expected_response = hash_response(nonce, shared_secret, client_id)

if client_response == expected_response:
    print("Authentication Successful")
else:
    print("Authentication Failed")

timestamp = str(int(time.time()))
nonce_with_time = nonce + timestamp
response_with_time = hmac.new(shared_secret.encode(), (nonce_with_time + client_id).encode(), hashlib.sha256).hexdigest()
print("Client sends encrypted response with timestamp:", response_with_time)

current_time = int(time.time())
received_time = int(timestamp)

if abs(current_time - received_time) <= 5:
    expected_response_time = hmac.new(shared_secret.encode(), (nonce + timestamp + client_id).encode(), hashlib.sha256).hexdigest()
    if response_with_time == expected_response_time:
        print("Authentication Successful with replay protection")
    else:
        print("Authentication Failed")
else:
    print("Replay attack detected - timestamp expired")
