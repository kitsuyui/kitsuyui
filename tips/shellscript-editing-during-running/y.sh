#!/bin/sh
set -eu
cat > run.sh <<EOT
#!/bin/sh
sleep 3
EOT
chmod +x run.sh
./run.sh &
cp -p run.sh run.sh.tmp
mv run.sh.tmp run.sh
echo 'echo Hello' >> run.sh
wait
rm run.sh
