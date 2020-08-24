Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
    apt-get -y update && apt-get -y upgrade
    apt-get install -y \
      python-pip \
      python-virtualenv
  SHELL

end
