import requests, json, os, yaml, sys
#
# This python script reads an ansible host inventory file like the following:
# ---
# all:
#   children:
#     jump:
#       hosts:
#         172.16.1.4:
#     controller:
#       hosts:
#         172.16.1.5:
#         172.16.1.6:
#         172.16.1.7:
#   vars:
#     ansible_user: "avi"
#     ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.azure"
#
# and creates a json output like the following when there is only one controller
#
# {
#     "avi_credentials": {
#         "api_version": "18.2.8",
#         "clusterFollowerOne": "",
#         "clusterFollowerTwo": "",
#         "clusterName": "avi-cluster",
#         "clusterStatus": "0",
#         "controller": "192.168.1.156",
#         "password": "Avi2020",
#         "username": "admin"
#     }
# }
#
#
# and creates a json output like the following when there are three controllers
#
# {
#     "avi_credentials": {
#         "api_version": "18.2.8",
#         "clusterFollowerOne": "192.168.1.156",
#         "clusterFollowerTwo": "192.168.1.158",
#         "clusterName": "avi-cluster",
#         "clusterStatus": "1",
#         "controller": "192.168.1.157",
#         "password": "Avi2020",
#         "username": "admin"
#     }
# }

hostFile = sys.argv[1]
password = sys.argv[2]
#version = sys.argv[3]
# outputFile = sys.argv[4]
username = 'admin'
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
controllerLeader = [*data_loaded['all']['children']['controller']['hosts']][0]
controllerFollower = []
if len([*data_loaded['all']['children']['controller']['hosts']]) == 1:
  #avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster': False}
  #avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version, 'clusterStatus': '0', 'clusterName': 'avi-cluster', 'clusterFollowerOne': '', 'clusterFollowerTwo': ''}}
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, \
                      'username': username, 'password': password, 'clusterStatus': '0', \
                      'clusterName': 'avi-cluster', 'clusterFollowerOne': '', \
                      'clusterFollowerTwo': ''}}
if len([*data_loaded['all']['children']['controller']['hosts']]) == 3:
  controllerFollower.append([*data_loaded['all']['children']['controller']['hosts']][1])
  controllerFollower.append([*data_loaded['all']['children']['controller']['hosts']][2])
  #avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster_status': '1', 'avi_cluster': {'name': 'avi-cluster', 'follower': controllerFollower }}
  #avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version, 'clusterStatus': '1', 'clusterName': 'avi-cluster', 'clusterFollowerOne': controllerFollower[0], 'clusterFollowerTwo': controllerFollower[1] }}
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, \
                      'username': username, 'password': password, 'clusterStatus': '1', \
                      'clusterName': 'avi-cluster', 'clusterFollowerOne': controllerFollower[0], \
                      'clusterFollowerTwo': controllerFollower[1] }}
# with open(outputFile, 'w') as outfile:
#   yaml.dump(avi_credentials, outfile, default_flow_style=False)
#   outfile.close
print(json.dumps(avi_credentials))
