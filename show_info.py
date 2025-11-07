def show_info(*args):
    print(f"{len(args)} arguments were received.")
    print("The values are:", args)

show_info(4, 5, 6)