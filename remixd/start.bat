set SRC=%cd%\contracts
echo Hosting remixd with smart contracts at %SRC%
docker run -v %SRC%:/home/node/source -p 65520:65520 --name remixd -d remixd:latest
