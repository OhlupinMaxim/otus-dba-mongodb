userDatabase='aci_db'
userName='aci_user'
userPassword='12345'
# shellcheck disable=SC2089
mongoScript="db=db.getSiblingDB('$userDatabase');db.createUser({ user: '$userName', pwd: '$userPassword', roles: [ { role: 'readWrite', db: '$userDatabase' } ] });"

mongosh admin -u root -p root --eval "${mongoScript}"