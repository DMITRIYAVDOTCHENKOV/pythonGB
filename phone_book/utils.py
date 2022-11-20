from phone_book.models import User, Phone


def phone_saver(name: str, phones: str) -> bool:
    if name and phones:
        user = User.add(name)
        for phone in phones.split("\n"):
            Phone.add(phone, user)
        return True
    return False


def show_all_phones() -> list:
    return [tuple([user.name, ", ".join([phone.phone for phone in user.phones]), user.id]) for user in User.all()]


def show_all_for_name(name: str) -> list:
    print(name)
    return [tuple([user.name, " ".join([phone.phone for phone in user.phones]), user.id]) for user in
            User.find_by_name(name)]


def show_all_for_phone(phone: str) -> list:
    res = [tuple([user.name, " ".join([phone.phone for phone in user.phones]), user.id]) for user in
           User.find_by_phone(phone)]
    return res
