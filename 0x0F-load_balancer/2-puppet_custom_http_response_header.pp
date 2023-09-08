# add redirection and error page
exec { 'add_header';
  command      => 'sudo apt-get -y update;
  sudo apt-get -y  install nginx;
  sudo sed -i '/server_name _;/a \\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t}\n\terror_page 404 /404.html;\n\tlocation \/404.html {\n\t\tinternal;\n}' /etc/nginx/sites-available/default;
  sudo service nginx restart;',
  provider     => shell,
  refresh only => true,
}
