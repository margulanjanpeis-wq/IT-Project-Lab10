
# Тіркелген өндірістік немесе стендтік инциденттер
incidents = []

if not incidents:
    print("Тіркелген инциденттер саны: 0")
    print("Recovery Time: N/A")
    print("Себебі: қалпына келтіруді қажет еткен ақау жоқ.")
else:
    recovery_times = [
        incident["recovery_minutes"]
        for incident in incidents
    ]

    import statistics

    median_time = statistics.median(recovery_times)

    print(f"Recovery Time: {median_time:.1f} минут")
