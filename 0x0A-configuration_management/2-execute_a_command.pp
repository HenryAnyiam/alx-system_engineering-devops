#execute a command
exec { 'kill_a_process':
  command => 'pkill killmenow'
}
