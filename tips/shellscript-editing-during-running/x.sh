#!/bin/sh
set -eu
cat > run.sh <<EOT
#!/bin/sh
sleep 3
EOT
chmod +x run.sh
./run.sh &
echo 'echo Hello' >> run.sh
wait
rm run.sh
