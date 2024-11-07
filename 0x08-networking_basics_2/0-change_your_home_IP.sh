#!/usr/bin/env bash

# This script configures the local host and facebook.com DNS resolution

# Update /etc/hosts file to resolve localhost to 127.0.0.2
echo "127.0.0.2 localhost" | sudo tee /etc/hosts

# Update /etc/hosts file to resolve facebook.com to 8.8.8.8
echo "8.8.8.8 facebook.com" | sudo tee -a /etc/hosts
