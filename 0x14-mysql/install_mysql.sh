#!/usr/bin/env bash
# Script to install MySQL 5.7 on Ubuntu servers

# Add MySQL apt repository
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
dpkg -i mysql-apt-config_0.8.12-1_all.deb

# Update apt
apt-get update

# Install MySQL 5.7
apt-get install -y mysql-server=5.7* mysql-client=5.7*

# Secure MySQL installation
mysql_secure_installation

# Enable MySQL service
systemctl enable mysql
systemctl start mysql

# Clean up downloaded files
rm mysql-apt-config_0.8.12-1_all.deb

# Verify installation
mysql --version
