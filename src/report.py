# src/report.py

def print_user_report(user):
    print("---------- USER REPORT ----------")
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Age:", user["age"])
    print("---------------------------------\n")


def print_order_report(order):
    print("---------- ORDER REPORT ----------")
    print("Order ID:", order["id"])
    print("Total:", order["total"])
    print("Status:", order["status"])
    print("-----------------------------------\n")
    def _print_report(title, entries):
        header = f"---------- {title} ----------"
        print(header)
        for label, value in entries:
            print(f"{label}:", value)
        print("-" * len(header))
        print()

    def print_user_report(user):
        _print_report(
            "USER REPORT",
            [
                ("Name", user["name"]),
                ("Email", user["email"]),
                ("Age", user["age"]),
            ],
        )

    def print_order_report(order):
        _print_report(
            "ORDER REPORT",
            [
                ("Order ID", order["id"]),
                ("Total", order["total"]),
                ("Status", order["status"]),
            ],
        )