# Puppet manifest to install Flask 2.1.0 and compatible Werkzeug using pip3
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}
