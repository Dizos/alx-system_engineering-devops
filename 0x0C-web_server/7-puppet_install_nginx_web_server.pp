# Puppet manifest to install and configure nginx

# Update package manager
exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update']
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx']
}

# Add nginx configuration for redirect
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    location / {
        try_files \$uri \$uri/ =404;
    }
}",
  require => Package['nginx']
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default']
}
