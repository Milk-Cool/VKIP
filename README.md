# VKIP
Gets a Vkontakte user's IP address via a P2P call

# Tutorial
1. Install Python.
2. Install `mitmproxy` using `pip3 install mitmproxy` (or `pip install mitmproxy` on Windows)
3. Download the file `vkip.py`.
4. In the same directory (folder), run `mitmproxy -s vkip.py` in your terminal.
5. In your Android phone's WiFi settings, specify your computer's IP address and port 8080.
6. Follow [this tutorial](https://gist.github.com/stefanstranger/7a17b53e0bc3d354e94774420ec406a2) to install the `mitmproxy` certificate on your phone.
7. Open the VK app on your phone and call someone.
8. Wait until they pick up.
9. Hang up and wait 10 seconds.
10. On your computer, open the `mitmproxy` logs using Shift+E and look for `Captured IP address: X.X.X.X`. That's the IP of the person you just called.