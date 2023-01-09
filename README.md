batchspawner-portwrap
=====================

This script can be used by JupyterHub's
[batchspawner](https://github.com/jupyterhub/batchspawner) to execute
jupyterhub-singleuser inside a sandbox. The use case would be if you:

 - run jupyterhub,
 - use batchspawner to launch jupyter servers on multi-user systems,
 - configure the singleuser environment to proxy apps via jupyter-server-proxy,
 - need to protect access to proxied apps from any user on the system.

Ordinarily, apps proxied by jupyter-server-proxy run on open localhost ports,
and when accessed directly (not through the proxy URL) they may not require
authentication. For example while `{hub_url}/user/{username}/{proxied_app}`
requires authentication via jupyter server, the proxied app would still be
listening on an open TCP port on localhost. Any other user on the system can
connect to it from any TCP or HTTP client.

`batchspawner-portwrap` uses [portwrap](https://github.com/ryanlovett/portwrap)
to prepare a sandbox with user and network namespaces, and runs
`jupyterhub-singleuser` inside it. The jupyter server continues to accept
authenticated connections to its port, but proxied services are only reachable
by other programs running in the sandbox. Users on the system are not able to
reach those apps.

`batchspawner-singleuser` determines a random port number available on the
execution host and passes it to `jupyterhub-singleuser`. We intercept that
parameter and pass it to portwrap instead, which then calls
`jupyterhub-singleuser`. Jupyter server listens on that port (and only that
port) outside the sandbox, but listens on the default jupyter server port
inside it.


Installation
------------
```shell
pip install git+https://github.com/ryanlovett/batchspawner-portwrap
```


Configuration
-------------
In your jupyterhub configuration, insert `batchspawner-portwrap` in front of your `c.Spawner.cmd`. For example, if you have set something like:

```python
c.Spawner.cmd = [
    'jupyterhub-singleuser', '--arg1', '--arg2', ...
]
```

Replace it with:
```python
c.Spawner.cmd = [
    'batchspawner-portwrap', 'jupyterhub-singleuser', '--arg1', '--arg2', ...
]
```
