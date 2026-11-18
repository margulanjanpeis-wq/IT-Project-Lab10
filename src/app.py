
def calculate_priority(urgency, impact):
    """Өтінімнің маңыздылық деңгейін есептеу."""
    return urgency * impact


def get_status(priority):
    """Өтінімнің басымдық санатын анықтау."""
    if priority >= 15:
        return "Жоғары"
    elif priority >= 8:
        return "Орташа"
    return "Төмен"


if __name__ == "__main__":
    priority = calculate_priority(4, 5)
    print("Өтінімнің басымдылығы:", get_status(priority))
