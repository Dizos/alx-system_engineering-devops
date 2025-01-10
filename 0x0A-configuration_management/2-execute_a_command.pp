# Kills a process named killmenow using pkill command

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep killmenow',
}
