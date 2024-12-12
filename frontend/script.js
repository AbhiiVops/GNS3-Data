document.getElementById('addDeviceBtn').addEventListener('click', addDevice);
document.getElementById('removeDeviceBtn').addEventListener('click', removeDevice);

function addDevice() {
    const data = {
        "node_type": "dynamips",
        "compute_id": "local",
        "name": "R1",
        "properties": {
            "platform": "c7200",
            "nvram": 512,
            "image": "c7200-adventerprisek9-mz.153-3.XB12.image",
            "ram": 512,
            "slot0": "C7200-IO-FE",
            "slot1": "PA-GE",
            "slot2": "PA-GE",
            "slot3": "PA-GE",
            "system_id": "FTX0945W0MY",
            "idlepc": "0x606e0538"
        },
        "symbol": ":/symbols/router.svg",
        "x": 400,
        "y": 400
    };

    fetch('http://localhost:5000/add_device', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerHTML = `Node Created: ${data.node_id}`;
    })
    .catch(error => {
        document.getElementById('response').innerHTML = `Error: ${error.message}`;
    });
}

function removeDevice() {
    const nodeId = prompt("Enter Node ID to Remove:");

    fetch('http://localhost:5000/remove_device', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "node_id": nodeId })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerHTML = `Node Removed: ${nodeId}`;
    })
    .catch(error => {
        document.getElementById('response').innerHTML = `Error: ${error.message}`;
    });
}
