
deployments = 1

print("Барлық сәтті орналастыру саны:", deployments)

answer = input(
    "Орналастырудан кейін ақау болды ма? (иә/жоқ): "
).strip().lower()

if answer in ("иә", "ия", "yes"):
    failed = 1
elif answer in ("жоқ", "жок", "no"):
    failed = 0
else:
    raise ValueError("Иә немесе жоқ деп жауап беріңіз.")

cfr = failed / deployments * 100

print(f"Change Failure Rate: {cfr:.1f}%")
