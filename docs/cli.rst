Command-line interpreter
========================

The transip-api includes a command-line interpreter (CLI) that doesn't do much
yet. By default it does a `getDomainNames()` call, but with the `-u` option
it's also possible to add or update DNS records. When calling it with the `-h`,
it will show all available options.

.. code-block:: bash

   $ transip-api
   [example.com, example.org, example.net]

   $ transip-api -h
   usage: transip-api [-h] [-l LOGINNAME] [-s] [-a] [-u] [-d]
                      [--domain-name DOMAIN_NAME] [--entry-name ENTRY_NAME]
                      [--entry-expire ENTRY_EXPIRE] [--entry-type ENTRY_TYPE]
                      [--entry-content ENTRY_CONTENT] [--api-key PRIVATE_KEY_FILE]

   optional arguments:
     -h, --help            show this help message and exit
     -l LOGINNAME, --login-name LOGINNAME
                           TransIP username
     -s, --show-dns-entries
                           show all DNS entries for a domain
     -a, --add-dns-entry   add an entry in the DNS
     -u, --update-dns-entry
                           update an entry in the DNS
     -d, --delete-dns-entry
                           delete an entry in the DNS
     --domain-name DOMAIN_NAME
                           domain name to use
     --entry-name ENTRY_NAME
                           name of the DNS entry
     --entry-expire ENTRY_EXPIRE
                           expire time of the DNS entry
     --entry-type ENTRY_TYPE
                           type of the DNS entry
     --entry-content ENTRY_CONTENT
                           content of the DNS entry
     --api-key PRIVATE_KEY_FILE
                           TransIP private key

Example of adding/updating a record:

.. code-block:: bash

   $ transip-api -l githubuser -u --api-key privatekey --domain-name example.com --entry-name testentry --entry-expire 86400 --entry-type A --entry-content 127.0.0.1
   Request finished successfully.
