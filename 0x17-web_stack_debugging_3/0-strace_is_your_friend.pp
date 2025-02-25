# This Puppet manifest fixes an Apache 500 error caused by a typo in a PHP file path
# The issue was identified using strace and shows a file extension typo (.phpp instead of .php)

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/usr/bin:/bin',
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
}
