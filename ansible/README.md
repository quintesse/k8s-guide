
Ansible setup:

```
$ ansible-galaxy collection install ansible.posix
$ ansible-galaxy collection install community.general
$ ansible-galaxy collection install community.kubernetes
```

Installing/updating the K8s cluster:

```
$ ansible-playbook k8s-kubeadm.yml -i hosts
```
