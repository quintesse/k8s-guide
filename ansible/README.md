
Ansible setup:

```
$ ansible-galaxy collection install ansible.posix
$ ansible-galaxy collection install community.general
```

Installing/updating the K8s cluster:

```
$ ansible-playbook site.yml -i hosts
```

