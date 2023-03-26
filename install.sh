#!/bin/bash
echo "Creating directory.."
mkdir /etc/secondscron
echo "Copying files.."
cp main.py /etc/secondscron
# Create a Systemd unit file for your Python script
echo "Creating service.."
cat > /etc/systemd/system/secondscron.service << EOF
[Unit]
Description=Seconds Cron
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/etc/secondscron
ExecStart=python3 /etc/secondscron/main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload Systemd to pick up the new unit file
systemctl daemon-reload

# Start the service
echo "staring service.."
systemctl start secondscron

# Enable the service to start on boot
systemctl enable secondscron
echo "service name is 'secondscron'"
echo "[+] Installation completed"
