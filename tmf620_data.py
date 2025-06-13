catalogs = [
  {
    "id": "1",
    "name": "4G Mobile Services",
    "description": "Catalog for legacy 4G mobile offerings.",
    "version": "1.0",
    "lastUpdate": "2025-01-01T00:00:00Z",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-01-01T00:00:00Z",
      "endDateTime": "2026-01-01T00:00:00Z"
    }
  },
  {
    "id": "2",
    "name": "5G Ultra Network",
    "description": "Latest 5G services with low latency and high speed.",
    "version": "2.1",
    "lastUpdate": "2025-03-15T12:00:00Z",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2025-01-01T00:00:00Z",
      "endDateTime": "2027-12-31T23:59:59Z"
    }
  },
  {
    "id": "3",
    "name": "Fiber Optic Broadband",
    "description": "Catalog for FTTH and FTTB fiber products.",
    "version": "3.0",
    "lastUpdate": "2025-04-10T08:30:00Z",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-06-01T00:00:00Z",
      "endDateTime": "2026-06-01T00:00:00Z"
    }
  },
  {
    "id": "4",
    "name": "DSL Internet Services",
    "description": "Standard ADSL/VDSL packages for residential users.",
    "version": "1.5",
    "lastUpdate": "2025-02-20T09:00:00Z",
    "lifecycleStatus": "Deprecated",
    "validFor": {
      "startDateTime": "2023-01-01T00:00:00Z",
      "endDateTime": "2025-12-31T23:59:59Z"
    }
  },
  {
    "id": "5",
    "name": "Satellite Connectivity",
    "description": "Internet and voice services for remote areas using satellite links.",
    "version": "1.2",
    "lastUpdate": "2025-05-01T15:45:00Z",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-09-01T00:00:00Z",
      "endDateTime": "2027-09-01T00:00:00Z"
    }
  }
]

offerings = [
  {
    "id": "1001",
    "name": "4G Basic Plan",
    "description": "Includes 5GB data, 500 mins, 100 texts. Ideal for light users.",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-01-01T00:00:00Z",
      "endDateTime": "2026-01-01T00:00:00Z"
    },
    "category": [{"name": "Mobile Plans", "id": "cat1"}],
    "productSpecification": {
      "id": "spec-4g-basic",
      "name": "4G Mobile Specification"
    }
  },
  {
    "id": "1002",
    "name": "5G Unlimited Plan",
    "description": "Unlimited data, voice, and texts. Includes priority network access.",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2025-01-01T00:00:00Z",
      "endDateTime": "2027-01-01T00:00:00Z"
    },
    "category": [{"name": "Mobile Plans", "id": "cat2"}],
    "productSpecification": {
      "id": "spec-5g-ultra",
      "name": "5G Network Specification"
    }
  },
  {
    "id": "1003",
    "name": "Fiber Home 1Gbps",
    "description": "Unlimited 1Gbps fiber internet. Free installation included.",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-06-01T00:00:00Z",
      "endDateTime": "2026-06-01T00:00:00Z"
    },
    "category": [{"name": "Broadband", "id": "cat3"}],
    "productSpecification": {
      "id": "spec-fiber1g",
      "name": "FTTH Broadband Spec"
    }
  },
  {
    "id": "1004",
    "name": "DSL Family Plan",
    "description": "20Mbps ADSL line for standard home use.",
    "lifecycleStatus": "Deprecated",
    "validFor": {
      "startDateTime": "2023-01-01T00:00:00Z",
      "endDateTime": "2025-12-31T23:59:59Z"
    },
    "category": [{"name": "Broadband", "id": "cat4"}],
    "productSpecification": {
      "id": "spec-dsl20mb",
      "name": "DSL Internet Specification"
    }
  },
  {
    "id": "1005",
    "name": "Satellite Essentials",
    "description": "50GB per month with voice add-on. For rural connectivity.",
    "lifecycleStatus": "Active",
    "validFor": {
      "startDateTime": "2024-09-01T00:00:00Z",
      "endDateTime": "2027-09-01T00:00:00Z"
    },
    "category": [{"name": "Satellite Plans", "id": "cat5"}],
    "productSpecification": {
      "id": "spec-sat-basic",
      "name": "Satellite Connectivity Spec"
    }
  }
]


specifications = {
    "1": {
        "id": "spec-4g-basic",
        "name": "4G Mobile Specification",
        "description": "Technical specification for standard 4G plans.",
        "version": "1.0",
        "lifecycleStatus": "Active",
        "lastUpdate": "2024-12-01T12:00:00Z",
        "resourceSpecification": {
            "id": "res-4g-sim",
            "name": "4G SIM Resource"
        },
        "serviceSpecification": {
            "id": "svc-voice-data",
            "name": "Voice and Data Service"
        }
    },
    "2": {
        "id": "spec-5g-ultra",
        "name": "5G Network Specification",
        "description": "Supports low-latency, high-bandwidth 5G services.",
        "version": "2.2",
        "lifecycleStatus": "Active",
        "lastUpdate": "2025-05-10T10:30:00Z",
        "resourceSpecification": {
            "id": "res-5g-nr",
            "name": "5G NR Radio Resource"
        },
        "serviceSpecification": {
            "id": "svc-5g-stream",
            "name": "5G Stream and Slice"
        }
    },
    "3": {
        "id": "spec-fiber1g",
        "name": "FTTH Broadband Spec",
        "description": "Fiber-to-the-home 1Gbps connectivity specification.",
        "version": "3.0",
        "lifecycleStatus": "Active",
        "lastUpdate": "2025-02-20T08:15:00Z",
        "resourceSpecification": {
            "id": "res-fiber-ont",
            "name": "Optical Network Terminal"
        },
        "serviceSpecification": {
            "id": "svc-fiber-basic",
            "name": "Basic Fiber Internet Service"
        }
    },
    "4": {
        "id": "spec-dsl20mb",
        "name": "DSL Internet Specification",
        "description": "Standard 20Mbps ADSL/VDSL connection.",
        "version": "1.5",
        "lifecycleStatus": "Deprecated",
        "lastUpdate": "2023-11-10T09:00:00Z",
        "resourceSpecification": {
            "id": "res-dsl-modem",
            "name": "DSL Modem"
        },
        "serviceSpecification": {
            "id": "svc-dsl",
            "name": "DSL Internet Service"
        }
    },
    "5": {
        "id": "spec-sat-basic",
        "name": "Satellite Connectivity Spec",
        "description": "Low-throughput, high-latency satellite internet service.",
        "version": "1.1",
        "lifecycleStatus": "Active",
        "lastUpdate": "2025-04-01T11:45:00Z",
        "resourceSpecification": {
            "id": "res-sat-dish",
            "name": "Satellite Dish and Modem"
        },
        "serviceSpecification": {
            "id": "svc-sat-basic",
            "name": "Basic Satellite Service"
        }
    }
}


