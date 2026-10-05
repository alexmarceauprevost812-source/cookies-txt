<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TI-LEX CODEX</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 50px auto;
            background-color: #333;
            padding: 20px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        h1 {
            text-align: center;
            color: #fff;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 10px;
        }
        input[type="text"], input[type="submit"] {
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #555;
            border-radius: 5px;
            color: #fff;
            background-color: #444;
        }
        input[type="submit"] {
            background-color: #007BFF;
            color: #fff;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #555;
            border: 1px solid #333;
            border-radius: 5px;
            color: #fff;
        }
        .cookie-input {
            margin-top: 20px;
        }
        .attack-button {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>TI-LEX CODEX</h1>
        <form id="appInfoForm">
            <label for="macAddress">MAC Address:</label>
            <input type="text" id="macAddress" name="macAddress" readonly>
            <label for="openPort">Open Port:</label>
            <input type="text" id="openPort" name="openPort" readonly>
            <label for="cookies">Cookies:</label>
            <input type="text" id="cookies" name="cookies" readonly>
            <input type="submit" value="Get Information">
        </form>
        <div class="result" id="result"></div>
        <div class="cookie-input">
            <label for="cookieInput">Cookies:</label>
            <input type="text" id="cookieInput" name="cookieInput">
        </div>
        <div class="attack-button">
            <input type="submit" value="Attack Target" id="attackButton">
        </div>
    </div>

    <script>
        document.getElementById('appInfoForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const macAddress = getMacAddress();
            const openPort = findOpenPort();
            const cookies = get_cookies();

            document.getElementById('macAddress').value = macAddress;
            document.getElementById('openPort').value = openPort;
            document.getElementById('cookies').value = cookies;

            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `
                <p><strong>MAC Address:</strong> ${macAddress}</p>
                <p><strong>Open Port:</strong> ${openPort}</p>
                <p><strong>Cookies:</strong> ${cookies}</p>
            `;
        });

        document.getElementById('attackButton').addEventListener('click', function(event) {
            event.preventDefault();
            const target = document.getElementById('cookieInput').value;
            if (target) {
                alert(`Attacking target: ${target}`);
                // Add your attack logic here
            } else {
                alert('Please enter a target');
            }
        });

        function getMacAddress() {
            return ':'.join(['{:02x}'.format((Math.random() * 256) % 256) for i in range(6)]);
        }

        function findOpenPort() {
            const s = new WebSocket('ws://127.0.0.1:8080');
            s.onopen = () => {
                s.close();
                return 8080;
            };
            s.onerror = () => {
                return 5000;
            };
        }

        function get_cookies() {
            return "session_id=1234567890; user=admin";
        }
    </script>
</body>
</html>
