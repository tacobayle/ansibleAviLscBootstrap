# aviLsc

## Goals
This Ansible playbooks bootstrap Avi LSC controller without cluster configuration

## Prerequisites:
1. Make sure 1 or 3 Vm(s) has/have been deployed with the Avi software installed
2. Make sure avisdk is installed:
```
avi@ansible:~/ansible/aviLsc$ pip install avisdk==18.2.9
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

```
Avi 20.1.1
avisdk 18.2.9
```
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
api_version: 20.1.1
```

## Use the ansible playbook to
1. Wait for the Avi portal to be up
2. Generate variable to feed the python SDK
3. Update the password
4. Create accounts with auto-generated password for automation accounts
5. export the credentials to an external file for further usage


## Run the playbook:
ansible-playbook -i hosts main.yml

## Improvement:
Handle cluster configuration
