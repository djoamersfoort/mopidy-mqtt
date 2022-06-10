#!/bin/bash
sudo cp mqtt-daemon.service /etc/systemd/system/mqtt-daemon.service
sudo systemctl daemon-reload
sudo systemctl enable mqtt-daemon.service
sudo systemctl start mqtt-daemon.service