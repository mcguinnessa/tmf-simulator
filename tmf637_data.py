product_inventory = {
    "prod-001": {
        "id": "prod-001",
        "name": "4G Data Plan - 10GB",
        "description": "Monthly 4G data plan with 10GB allowance.",
        "productOffering": {
            "id": "1001",
            "name": "4G Basic Plan"
        },
        "productSpecification": {
            "id": "spec-4g-basic",
            "name": "4G Mobile Specification"
        },
        "status": "active",
        "startDate": "2025-01-10T00:00:00Z",
        "terminationDate": None,
        "productCharacteristic": [
            {"name": "Data Allowance", "value": "10GB"},
            {"name": "Voice Minutes", "value": "500"}
        ],
        "relatedParty": [
            {
                "role": "Customer",
                "id": "cust-100",
                "name": "Alice Example"
            }
        ]
    },
    "prod-002": {
        "id": "prod-002",
        "name": "5G Business Unlimited",
        "description": "Unlimited 5G data with business priority.",
        "productOffering": {
            "id": "1002",
            "name": "5G Unlimited Plan"
        },
        "productSpecification": {
            "id": "spec-5g-ultra",
            "name": "5G Network Specification"
        },
        "status": "active",
        "startDate": "2025-04-01T00:00:00Z",
        "terminationDate": None,
        "productCharacteristic": [
            {"name": "Speed Tier", "value": "Max"},
            {"name": "Priority Access", "value": "Yes"}
        ],
        "relatedParty": [
            {
                "role": "Customer",
                "id": "cust-200",
                "name": "ACME Corp"
            }
        ]
    },
    "prod-003": {
        "id": "prod-003",
        "name": "Fiber 1Gbps Residential",
        "description": "FTTH broadband at 1Gbps for residential user.",
        "productOffering": {
            "id": "1003",
            "name": "Fiber Home 1Gbps"
        },
        "productSpecification": {
            "id": "spec-fiber1g",
            "name": "FTTH Broadband Spec"
        },
        "status": "active",
        "startDate": "2024-11-15T00:00:00Z",
        "terminationDate": None,
        "productCharacteristic": [
            {"name": "Bandwidth", "value": "1Gbps"},
            {"name": "Usage Cap", "value": "Unlimited"}
        ],
        "relatedParty": [
            {
                "role": "Customer",
                "id": "cust-300",
                "name": "Bob Fiber"
            }
        ]
    },
    "prod-004": {
        "id": "prod-004",
        "name": "DSL Basic 20Mbps",
        "description": "ADSL connection for light home use.",
        "productOffering": {
            "id": "1004",
            "name": "DSL Family Plan"
        },
        "productSpecification": {
            "id": "spec-dsl20mb",
            "name": "DSL Internet Specification"
        },
        "status": "terminated",
        "startDate": "2023-03-01T00:00:00Z",
        "terminationDate": "2025-03-01T00:00:00Z",
        "productCharacteristic": [
            {"name": "Bandwidth", "value": "20Mbps"},
            {"name": "Modem Supplied", "value": "Yes"}
        ],
        "relatedParty": [
            {
                "role": "Customer",
                "id": "cust-400",
                "name": "Charlie DSL"
            }
        ]
    },
    "prod-005": {
        "id": "prod-005",
        "name": "Satellite Rural Access",
        "description": "Satellite internet for rural area with 50GB cap.",
        "productOffering": {
            "id": "1005",
            "name": "Satellite Essentials"
        },
        "productSpecification": {
            "id": "spec-sat-basic",
            "name": "Satellite Connectivity Spec"
        },
        "status": "active",
        "startDate": "2025-05-20T00:00:00Z",
        "terminationDate": None,
        "productCharacteristic": [
            {"name": "Monthly Cap", "value": "50GB"},
            {"name": "Latency", "value": "High"}
        ],
        "relatedParty": [
            {
                "role": "Customer",
                "id": "cust-500",
                "name": "RuralNet Solutions"
            }
        ]
    }
}
