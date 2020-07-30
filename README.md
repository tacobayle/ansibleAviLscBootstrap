# aviLsc

## Goals
This Ansible playbooks bootstrap Avi LSC controller without cluster configuration

## Prerequisites:
1. Make sure 1 or 3 Vm(s) has/have been deployed with the Avi software installed
2. Make sure avisdk is installed:
```
avi@ansible:~/ansible/aviLsc$ pip install avisdk==18.2.8
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Defaulting to user installation because normal site-packages is not writeable
Collecting avisdk==18.2.8
  Downloading avisdk-18.2.8.tar.gz (84 kB)
     |████████████████████████████████| 84 kB 366 kB/s
Requirement already satisfied: requests in /home/avi/.local/lib/python2.7/site-packages (from avisdk==18.2.8) (2.21.0)
Requirement already satisfied: certifi>=2017.4.17 in /home/avi/.local/lib/python2.7/site-packages (from requests->avisdk==18.2.8) (2018.11.29)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /home/avi/.local/lib/python2.7/site-packages (from requests->avisdk==18.2.8) (1.24.1)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /home/avi/.local/lib/python2.7/site-packages (from requests->avisdk==18.2.8) (3.0.4)
Requirement already satisfied: idna<2.9,>=2.5 in /home/avi/.local/lib/python2.7/site-packages (from requests->avisdk==18.2.8) (2.8)
Building wheels for collected packages: avisdk
  Building wheel for avisdk (setup.py) ... done
  Created wheel for avisdk: filename=avisdk-18.2.8-py2-none-any.whl size=109125 sha256=419583b9cbc8d1392e664a676e6c4349f7008803872099882c7640842157e8c1
  Stored in directory: /home/avi/.cache/pip/wheels/41/c4/49/857ee121ef1f2f6098be85838d1128c4a9dd974e1c80489629
Successfully built avisdk
Installing collected packages: avisdk
  Attempting uninstall: avisdk
    Found existing installation: avisdk 18.1.5b3
    Uninstalling avisdk-18.1.5b3:
      Successfully uninstalled avisdk-18.1.5b3
Successfully installed avisdk-18.2.8
WARNING: You are using pip version 20.0.2; however, version 20.1.1 is available.
You should consider upgrading via the '/usr/bin/python -m pip install --upgrade pip' command.
avi@ansible:~/ansible/aviLsc$
avi@ansible:~/ansible/aviLsc$
avi@ansible:~/ansible/aviLsc$ ansible-galaxy install -f avinetworks.avisdk
- changing role avinetworks.avisdk from 18.2.1 to unspecified
- downloading role 'avisdk', owned by avinetworks
- downloading role from https://github.com/avinetworks/ansible-role-avisdk/archive/18.2.8-beta.tar.gz
- extracting avinetworks.avisdk to /home/avi/.ansible/roles/avinetworks.avisdk
- avinetworks.avisdk (18.2.8-beta) was installed successfully
avi@ansible:~/ansible/aviLsc$

```

## Environment:

Playbook(s) has/have been tested against:

### Ansible

```
avi@ansible:~/aviLsc$ ansible --version
ansible 2.9.5
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/avi/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /home/avi/.local/lib/python2.7/site-packages/ansible
  executable location = /home/avi/.local/bin/ansible
  python version = 2.7.12 (default, Oct  8 2019, 14:14:10) [GCC 5.4.0 20160609]
avi@ansible:~/aviLsc$
```

### Avi version

docker_install-18.2.8-9205.tar.gz

## Input/Parameters:

1. An inventory file with the following format (could be 1 or 3 controller hosts):

```
---
all:
  children:
    se:
      hosts:
        192.168.142.129:
        192.168.142.130:
    controller:
      hosts:
        192.168.142.135:


  vars:
    ansible_user: avi
    ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.local"

```

2. All the paramaters/variables are stored in var/params.yml

3. The avi version should be stored in vars/aviVersion:
```
api_version: 18.2.8
```

## Use the ansible playbook to
1. Wait for the Avi portal to be up
2. Generate variable to feed the python SDK
3. Update the password
4. Create accounts with aito-generated password for automation accounts
5. Create a security passphrase for the backup
6. Configure glocal config.
7. export the credentials to an external file for further usage


## Run the playbook:
ansible-playbook -i hosts main.yml

## Improvement:
Handle cluster configuration
