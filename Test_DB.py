from ibm_db import connect
# Careful with the punctuation here - we have 3 arguments.
# The first is a big string with semicolons in it.
# (Strings separated by only whitespace, newlines included,
#  are automatically joined together, in case you didn't know.)
# The last two are emptry strings.
connection = connect('DATABASE=pps2qa;'
                     'HOSTNAME=dbsp8110;'  # 127.0.0.1 or localhost works if it's local
                     'PORT=50002;'
                     'PROTOCOL=TCPIP;'
                     'UID=PADMIMP;'
                     'PWD=SNQdVd9P;', '', '')
