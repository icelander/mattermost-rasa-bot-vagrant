# -*- mode: ruby -*-
# vi: set ft=ruby :

MATTERMOST_VERSION = "5.32.1"

MYSQL_ROOT_PASSWORD = 'mysql_root_password'
MATTERMOST_PASSWORD = 'really_secure_password'

ELASTICSEARCH_SERVERS = 3

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"

  config.vm.provider :virtualbox do |v|
    v.memory = 4096
    v.cpus = 4
  end

  config.vm.network :private_network, ip: "192.168.1.100"
  config.vm.hostname = 'mattermost-rasa'

  config.vm.provision :docker do |d|
    d.run 'mariadb', 
      image: 'mariadb',
      args: "-p 3306:3306\
             -e MYSQL_ROOT_PASSWORD=#{MYSQL_ROOT_PASSWORD}\
             -e MYSQL_USER=mmuser\
             -e MYSQL_PASSWORD=#{MATTERMOST_PASSWORD}\
             -e MYSQL_DATABASE=mattermost"
    d.run 'ldap',
      image: 'rroemhild/test-openldap',
      args: "-p 389:10389"
    # d.run 'rasa',
    #   image: 'rasa/rasa:2.1.2',
    #   cmd: 'init --no-prompt',
    #   args: "-p 5005:5005\
    #          -v /vagrant/rasa:/app"
  end

  config.vm.provision :shell, inline: 'apt-get update && apt-get upgrade -y'

  config.vm.provision :shell,
    path: 'rasa_setup.sh'
 
  config.vm.provision :shell,
    path: 'haproxy.sh'

  config.vm.provision 'shell',
    path: "setup.sh",
    args: [MATTERMOST_VERSION, MYSQL_ROOT_PASSWORD, MATTERMOST_PASSWORD]
end
