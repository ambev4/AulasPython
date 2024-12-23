#Exemplo de um array utilizado em Definitions file em pod de kubernets

spec = {
    "containers": [
        {"name": "httpd-container",
        "image": "httpd",
        "ports": [
            {"name": "http-port",
            "containerport": 80},
            {"name": "https-port",
            "containerport": 433}
            ]
        },
        {"name": "db-container",
        "image": "mysql",
        "ports": [
            {"name": "http-port",
            "containerport": 80}
            ]
        }
    ]
}

print(spec)