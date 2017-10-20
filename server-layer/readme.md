# Intermediate layer for server communication

## Instructions

1. Copy the `server-layer` folder to `/var/www/`. Rename it to `LDD_middle_layer`.
2. Copy `LDD_middle_layer.conf` to `/etc/apache2/sites-available/`.
3. Make sure `flask` is installed. This runs on Python 2.7.
4. Register the wsgi: `sudo a2ensite LDD_middle_layer`.
   If this leads to server crash, de-register it with `sudo a2dissite LDD_middle_layer`.
5. Reload Apache: `sudo service apache2 reload`
6. Test site: [https://www.plantbreeding.wur.nl/ld-demonstrator/](https://www.plantbreeding.wur.nl/ld-demonstrator/)

Likely to need modification:
* `ServerName` in `/etc/apache2/sites-available/LDD_middle_layer.conf`.
This is the hostname where the query is submitted. It is assumed that this is `plantbreeding.wur.nl`, which should also be in the hosts file. Multiple ServerNames can be declared, each on a separate line.
* line 87 in `__init__.py`:
`reqText = 'http://snowball:8890/sparql?format=json&query=' + urllib.quote(queryText)`
indicating the address of the machine hosting Virtuoso.
